"""
test_notes_app.py

Testing concepts demonstrated here (Week 1 checklist):

1. unittest basics       -> TestNoteDataclass (uses unittest.TestCase directly,
                             so you can see the assertEqual/assertRaises style
                             next to the pytest style below for comparison)
2. pytest fixtures        -> `manager` fixture below, using tmp_path
3. pytest.mark.parametrize -> test_add_note_rejects_invalid_titles,
                              test_search_notes_various_queries
4. pytest.raises          -> every "should fail" test
5. Debugging patterns      -> see debugging_notes.md for the write-up;
                              test_debug_example shows a deliberately-failing
                              case commented with how you'd diagnose it
"""

import json
import unittest

import pytest

from notes_app import NotesManager, Note, NoteNotFoundError, InvalidNoteError


# ---------------------------------------------------------------------------
# Part 1: plain unittest style (no pytest features) — for comparison
# ---------------------------------------------------------------------------

class TestNoteDataclass(unittest.TestCase):
    """Exercises the Note dataclass directly, unittest-style."""

    def test_to_dict_round_trip(self):
        note = Note(id=1, title="Groceries", body="milk, eggs", tags=["home"])
        as_dict = note.to_dict()
        rebuilt = Note.from_dict(as_dict)

        self.assertEqual(rebuilt.id, note.id)
        self.assertEqual(rebuilt.title, note.title)
        self.assertEqual(rebuilt.tags, ["home"])

    def test_from_dict_defaults_missing_fields(self):
        # Simulates loading an old/partial JSON record.
        note = Note.from_dict({"id": 5, "title": "Bare note"})
        self.assertEqual(note.body, "")
        self.assertEqual(note.tags, [])


# ---------------------------------------------------------------------------
# Part 2: pytest style — fixtures, parametrize, raises
# ---------------------------------------------------------------------------

@pytest.fixture
def manager(tmp_path):
    """
    Fresh NotesManager backed by a temp file for every test.

    tmp_path is a built-in pytest fixture: a unique pathlib.Path per test,
    auto-cleaned afterward. This is why tests never touch a real notes.json
    and never leak state between each other.
    """
    storage_file = tmp_path / "notes.json"
    return NotesManager(str(storage_file))


def test_add_note_returns_note_with_incrementing_id(manager):
    first = manager.add_note("First note")
    second = manager.add_note("Second note")

    assert first.id == 1
    assert second.id == 2


def test_add_note_persists_to_disk(manager):
    manager.add_note("Persisted note", body="check the file")

    with open(manager.storage_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["title"] == "Persisted note"


@pytest.mark.parametrize("bad_title", ["", "   ", None])
def test_add_note_rejects_invalid_titles(manager, bad_title):
    with pytest.raises(InvalidNoteError):
        manager.add_note(bad_title)


def test_get_note_missing_raises(manager):
    with pytest.raises(NoteNotFoundError):
        manager.get_note(999)


def test_delete_note_removes_it(manager):
    note = manager.add_note("Temporary")
    manager.delete_note(note.id)

    assert manager.list_notes() == []


def test_delete_note_missing_raises(manager):
    with pytest.raises(NoteNotFoundError):
        manager.delete_note(42)


def test_edit_note_updates_only_given_fields(manager):
    note = manager.add_note("Original title", body="original body")
    manager.edit_note(note.id, body="updated body")

    updated = manager.get_note(note.id)
    assert updated.title == "Original title"   # untouched
    assert updated.body == "updated body"       # changed


def test_edit_note_rejects_blank_title(manager):
    note = manager.add_note("Keep me")
    with pytest.raises(InvalidNoteError):
        manager.edit_note(note.id, title="   ")


@pytest.mark.parametrize(
    "query, expected_titles",
    [
        ("recipe", ["Pasta recipe"]),
        ("PASTA", ["Pasta recipe"]),          # case-insensitive
        ("nonexistent", []),
        ("", []),                              # empty query short-circuits
    ],
)
def test_search_notes_various_queries(manager, query, expected_titles):
    manager.add_note("Pasta recipe", body="tomato, garlic, basil")
    manager.add_note("Meeting notes", body="Q3 roadmap")

    results = manager.search_notes(query)
    assert [n.title for n in results] == expected_titles


def test_search_notes_matches_on_tags(manager):
    manager.add_note("Untitled", body="", tags=["urgent", "work"])
    results = manager.search_notes("urgent")
    assert len(results) == 1


def test_manager_reloads_existing_notes_from_disk(tmp_path):
    """Second manager pointed at the same file should see the first's notes."""
    storage_file = str(tmp_path / "notes.json")

    first_manager = NotesManager(storage_file)
    first_manager.add_note("Survives reload")

    second_manager = NotesManager(storage_file)
    notes = second_manager.list_notes()

    assert len(notes) == 1
    assert notes[0].title == "Survives reload"


# ---------------------------------------------------------------------------
# Part 3: a worked debugging example
# ---------------------------------------------------------------------------

def test_next_id_after_deleting_highest_id_note(manager):
    """
    This test is written the way you'd write it WHILE debugging a real bug:
    start from a suspicious behavior, assert what you expect, and let the
    failure message tell you exactly where the assumption broke.

    Bug scenario: if _next_id were computed fresh from max(existing ids)
    every time instead of tracked incrementally, deleting the
    highest-numbered note would cause the next add_note() to reuse an id.
    This test pins the correct behavior (ids are never reused) so that
    regression would fail loudly instead of silently corrupting data.
    """
    note_a = manager.add_note("A")
    note_b = manager.add_note("B")
    manager.delete_note(note_b.id)  # delete the highest id (2)

    note_c = manager.add_note("C")

    assert note_c.id == 3, (
        f"Expected id 3 (ids should never be reused), got {note_c.id}. "
        "If this fails, check whether _next_id is being recalculated from "
        "current notes instead of tracked as a running counter."
    )
