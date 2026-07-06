"""Tests for the Task Tracker.

Run them with:  python -m unittest discover tests

These give you something real to keep green while you practice making changes.
A good habit: run the tests before you open a pull request.
"""

import os
import sys
import unittest

# Make the src/ folder importable regardless of where tests are run from.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import tasks  # noqa: E402


class TestTasks(unittest.TestCase):
    def test_add_task_assigns_sequential_ids(self):
        items = []
        first = tasks.add_task(items, "Buy milk")
        second = tasks.add_task(items, "Walk the dog")
        self.assertEqual(first["id"], 1)
        self.assertEqual(second["id"], 2)
        self.assertEqual(len(items), 2)

    def test_new_task_starts_not_done(self):
        items = []
        task = tasks.add_task(items, "Buy milk")
        self.assertFalse(task["done"])

    def test_complete_task_marks_done(self):
        items = []
        tasks.add_task(items, "Buy milk")
        completed = tasks.complete_task(items, 1)
        self.assertIsNotNone(completed)
        self.assertTrue(completed["done"])

    def test_complete_missing_task_returns_none(self):
        items = []
        self.assertIsNone(tasks.complete_task(items, 99))

    def test_format_task_shows_checkbox(self):
        task = {"id": 1, "text": "Buy milk", "done": False}
        self.assertEqual(tasks.format_task(task), "[ ] #1  Buy milk")
        task["done"] = True
        self.assertEqual(tasks.format_task(task), "[x] #1  Buy milk")


if __name__ == "__main__":
    unittest.main()
