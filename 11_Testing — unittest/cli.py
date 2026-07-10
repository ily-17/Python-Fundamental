"""
cli.py

Thin command-line wrapper around NotesManager. Deliberately dumb — all real
logic lives in notes_app.py so it can be unit tested without touching stdin.
"""

import sys
from notes_app import NotesManager, NoteNotFoundError, InvalidNoteError

STORAGE_PATH = "notes.json"


def main():
    manager = NotesManager(STORAGE_PATH)

    if len(sys.argv) < 2:
        print("Usage: python cli.py [add|list|delete|search] ...")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            title = input("Title: ")
            body = input("Body: ")
            note = manager.add_note(title, body)
            print(f"Added note #{note.id}: {note.title}")

        elif command == "list":
            for note in manager.list_notes():
                print(f"[{note.id}] {note.title}")

        elif command == "delete":
            note_id = int(sys.argv[2])
            manager.delete_note(note_id)
            print(f"Deleted note #{note_id}")

        elif command == "search":
            query = sys.argv[2]
            for note in manager.search_notes(query):
                print(f"[{note.id}] {note.title}")

        else:
            print(f"Unknown command: {command}")

    except InvalidNoteError as e:
        print(f"Invalid input: {e}")
    except NoteNotFoundError as e:
        print(f"Not found: {e}")


if __name__ == "__main__":
    main()
