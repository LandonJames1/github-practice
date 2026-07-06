# Practice Exercises 🏋️

Once you've been through [GITHUB_TUTORIAL.md](GITHUB_TUTORIAL.md) once, repeat the
branch → PR → merge loop with these. **Do each one on its own branch and open a
separate pull request.** Repetition is how the workflow becomes automatic.

### Beginner

1. **Add a `count` command** that prints how many tasks are not yet done.
   - Branch idea: `add-count-command`
2. **Improve the empty-list message** in `list` to be friendlier.
3. **Add your name to the README** in a new "Practiced by" section.

### Intermediate

4. **Add a `clear` command** that deletes all completed tasks.
5. **Add priorities** — let `add` take an optional `!high` flag and show a `⭐`
   next to high-priority tasks in `list`.
6. **Write a test** for one of the features above, and make sure
   `python -m unittest discover tests` passes before opening the PR.

### Collaboration practice (the realistic stuff)

7. **Open an Issue** on GitHub describing a feature you want, using the templates
   in `.github/ISSUE_TEMPLATE/`. Then reference it in your PR with
   "Closes #<issue-number>" and watch GitHub auto-close it when you merge.
8. **Create a merge conflict on purpose** and resolve it:
   - On branch `a`, change the usage message on one line and merge it to `main`.
   - On branch `b` (started before `a` merged), change the *same* line differently.
   - Open a PR for `b` — GitHub will report a conflict. Resolve it by running
     `git switch b`, `git merge main`, editing the conflicted file, then
     `git add` + `git commit`. Push again and watch the conflict clear.
9. **Review your own PR properly**: leave an inline comment requesting a change,
   push a follow-up commit that addresses it, then approve and merge.

### Stretch

10. **Add a GitHub Action** (`.github/workflows/tests.yml`) that runs the tests
    automatically on every pull request. When it's set up, your PRs will show a
    green check ✅ when tests pass. Search "GitHub Actions Python unittest" to
    find a starter, or ask for help.

Keep a little log below of what you've done — crossing things off is satisfying.

- [ ] Exercise 1
- [ ] Exercise 2
- [ ] Exercise 3
- [ ] Exercise 4
- [ ] Exercise 5
- [ ] Exercise 6
- [ ] Exercise 7
- [ ] Exercise 8
- [ ] Exercise 9
- [ ] Exercise 10
