# Debugging Notes — Week 1

Practical debugging techniques used while building and testing this project.

## 1. Let pytest's failure output do the work

Run a single failing test with `-v` to see exactly which assertion broke:

```bash
pytest test_notes_app.py::test_next_id_after_deleting_highest_id_note -v
```

pytest shows the actual vs. expected values automatically for plain
`assert` statements — no need for `assertEqual`-style messages unless you
want extra context (see the custom message in that test).

## 2. `-x` to stop at the first failure

When a change breaks several tests at once, `-x` stops the run at the first
failure instead of dumping 15 tracebacks:

```bash
pytest -x
```

## 3. Drop into the debugger on failure

```bash
pytest --pdb
```

This opens a `pdb` prompt at the point of failure, inside the actual test
context — you can inspect `manager._notes`, `note.id`, etc. live instead of
guessing from print statements.

## 4. `-s` to see print/debug output

pytest captures stdout by default. Add temporary `print()` calls to trace
values, then run with `-s` to actually see them:

```bash
pytest -s test_notes_app.py::test_add_note_persists_to_disk
```

## 5. Reproduce the bug as a test first

The pattern used in `test_next_id_after_deleting_highest_id_note`:
1. Describe the suspicious behavior in the docstring.
2. Write the assertion for what *should* happen.
3. Add a message explaining what to check if it fails.

This turns "I think there might be a bug here" into a permanent regression
guard, and is generally faster than manually re-triggering the bug in the
CLI every time.

## 6. Isolate state with fixtures, not manual cleanup

Early versions of these tests used a single shared `notes.json` — tests
started failing depending on run order because leftover notes changed the
expected ids. Switching to the `manager` fixture (built on pytest's
`tmp_path`) gives every test a clean, isolated file automatically, which
removed the whole class of "works alone, fails in the suite" bugs.
