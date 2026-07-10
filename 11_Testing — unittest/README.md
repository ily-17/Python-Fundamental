# Notes App — Week 1 (Testing: unittest/pytest basics + debugging)

A small CLI notes manager, built specifically to practice testing
fundamentals: unittest basics, pytest fixtures, parametrized tests,
`pytest.raises`, and debugging workflow.

## Project structure

```
notes_app_project/
├── notes_app.py        # core logic: NotesManager, Note, custom exceptions
├── cli.py               # thin CLI wrapper (not unit tested directly —
│                         #   intentionally dumb, all logic lives in notes_app.py)
├── test_notes_app.py    # the test suite (19 tests)
├── debugging_notes.md   # debugging techniques used/demonstrated
└── README.md
```

## Features

- Add, list, edit, delete, and search notes
- Tag support, case-insensitive search across title/body/tags
- JSON persistence to a file (path is injected, not hardcoded — this is
  what makes it testable without touching a real file)
- Custom exceptions (`NoteNotFoundError`, `InvalidNoteError`) instead of
  generic `Exception`, so failure modes are precise and testable

## Running it

```bash
python cli.py add
python cli.py list
python cli.py search groceries
python cli.py delete 1
```

## Running the tests

```bash
pip install pytest
pytest test_notes_app.py -v
```

Current status: **19/19 passing**.

Useful variants:
```bash
pytest -x              # stop at first failure
pytest -s              # show print() output (capture off)
pytest --pdb           # drop into debugger on failure
pytest -k "search"     # run only tests matching "search"
```

## What each test file section demonstrates

| Section | Concept | Example |
|---|---|---|
| `TestNoteDataclass` | plain `unittest.TestCase` | `assertEqual`, `assertRaises` style, for comparison against pytest style |
| `manager` fixture | pytest fixtures + `tmp_path` | every test gets an isolated temp-file-backed manager |
| `test_add_note_rejects_invalid_titles` | `@pytest.mark.parametrize` | one test body, three input cases |
| `test_search_notes_various_queries` | parametrize with expected outputs | table-driven testing |
| every `with pytest.raises(...)` test | exception testing | asserting *which* exception, not just "it failed" |
| `test_next_id_after_deleting_highest_id_note` | debugging-driven test | see `debugging_notes.md` |

## Design decisions worth noting

- **Dependency injection for storage path**: `NotesManager(storage_path)`
  takes the file path as a constructor argument rather than hardcoding
  `"notes.json"`. This one decision is what makes the whole test suite
  possible without mocking the filesystem — tests just pass a `tmp_path`
  fixture instead.
- **Logic/IO separation**: `cli.py` only handles `input()`/`print()`;
  `notes_app.py` never does either. This means 100% of the interesting
  logic is unit-testable without capturing stdin/stdout.
- **Specific exceptions over generic ones**: lets tests assert exact
  failure modes (`pytest.raises(InvalidNoteError)` vs. catching any
  `Exception`), which catches regressions where the *wrong* kind of error
  starts being raised.

## Next steps (Week 2 candidates)

- Add `pytest-cov` and check coverage (`pytest --cov=notes_app`)
- Mock `datetime.now()` to test `created_at` deterministically
- Add a `conftest.py` if fixtures need to be shared across multiple test files
