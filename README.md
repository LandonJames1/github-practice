# Task Tracker 📝

A tiny command-line task list, built as a **practice project for learning Git and GitHub**.

The code itself is deliberately simple — the point isn't the app, it's giving you a
real repository to clone, branch, edit, and open pull requests against.

> 👉 **New here? Start with [GITHUB_TUTORIAL.md](GITHUB_TUTORIAL.md).** It walks you
> through the whole workflow step by step.

---

## What it does

```
$ python src/tasks.py add "Buy milk"
Added task #1: Buy milk

$ python src/tasks.py add "Walk the dog"
Added task #2: Walk the dog

$ python src/tasks.py list
[ ] #1  Buy milk
[ ] #2  Walk the dog

$ python src/tasks.py done 1
Completed task #1: Buy milk

$ python src/tasks.py list
[x] #1  Buy milk
[ ] #2  Walk the dog
```

Tasks are stored in a local `tasks.json` file (ignored by Git — see `.gitignore`).

## Requirements

- Python 3.8 or newer. No third-party packages needed.

## Running it

```bash
python src/tasks.py list
```

## Running the tests

```bash
python -m unittest discover tests
```

## Project layout

| Path                  | What it is                                             |
|-----------------------|--------------------------------------------------------|
| `src/tasks.py`        | The whole application                                  |
| `tests/test_tasks.py` | Automated tests                                        |
| `GITHUB_TUTORIAL.md`  | **The main event** — a hands-on Git/GitHub walkthrough |
| `EXERCISES.md`        | Practice tasks to try on your own                      |
| `CONTRIBUTING.md`     | How contributions work (practice for real repos)       |
| `.github/`            | Pull request & issue templates GitHub reads            |

## License

MIT — see [LICENSE](LICENSE).
