# Contributing

This is a personal practice repo, but it follows the same conventions real
open-source projects use — that's the point. Practicing this flow here means
you'll know exactly what to do when you contribute to a real project.

## The workflow

1. **Create a branch** for your change — never commit directly to `main`.
   ```bash
   git switch -c short-description-of-change
   ```
2. **Make your change** and keep commits small and focused.
3. **Run the tests** and make sure they pass:
   ```bash
   python -m unittest discover tests
   ```
4. **Push** your branch and **open a pull request**.
5. Fill out the pull request template.
6. Get the PR **reviewed and approved**, then **merge** it.

## Commit message style

- Write in the present tense: "Add delete command", not "Added delete command".
- Keep the first line under ~50 characters; add detail in the body if needed.

## Branch naming

Use short, hyphenated, descriptive names:
- ✅ `add-count-command`, `fix-empty-list-message`
- ❌ `stuff`, `patch-1`, `my-changes`
