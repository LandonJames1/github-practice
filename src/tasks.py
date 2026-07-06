"""Task Tracker — a tiny command-line to-do list.

This is a practice project for learning Git and GitHub. The code is kept
intentionally small and readable so you can focus on the workflow around it:
cloning, branching, committing, and opening pull requests.

Usage:
    python src/tasks.py add "Some task"
    python src/tasks.py list
    python src/tasks.py done 1
"""

import json
import os
import sys

# Tasks are saved next to this file so the app works from any directory.
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "tasks.json")


def load_tasks():
    """Read the task list from disk, returning an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Write the task list back to disk."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, text):
    """Add a new task and return the created task dict."""
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "text": text, "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    """Mark a task as done. Returns the task, or None if the id was not found."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    return None


def format_task(task):
    """Turn a task into a display line like '[x] #1  Buy milk'."""
    box = "x" if task["done"] else " "
    return f"[{box}] #{task['id']}  {task['text']}"


def main(argv):
    if not argv:
        print("Usage: add <text> | list | done <id>")
        return 1

    command = argv[0]
    tasks = load_tasks()

    if command == "add":
        if len(argv) < 2:
            print("Please provide the task text, e.g. add \"Buy milk\"")
            return 1
        task = add_task(tasks, argv[1])
        save_tasks(tasks)
        print(f"Added task #{task['id']}: {task['text']}")

    elif command == "list":
        if not tasks:
            print("No tasks yet. Add one with: add \"Your task\"")
        for task in tasks:
            print(format_task(task))

    elif command == "done":
        if len(argv) < 2:
            print("Please provide the task id, e.g. done 1")
            return 1
        task = complete_task(tasks, int(argv[1]))
        if task is None:
            print(f"No task with id {argv[1]}")
            return 1
        save_tasks(tasks)
        print(f"Completed task #{task['id']}: {task['text']}")

    else:
        print(f"Unknown command: {command}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
