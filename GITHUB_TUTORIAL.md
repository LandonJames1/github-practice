# The Hands-On GitHub Tutorial 🚀

This walks you through the **core GitHub workflow** using this very repository:
clone → branch → commit → push → pull request → review → merge.

Take it slowly. Type the commands yourself instead of copy-pasting — the muscle
memory is the whole point.

---

## 0. One-time setup

**Install Git** (check if you already have it):

```bash
git --version
```

If that errors, install it from https://git-scm.com/downloads (or `brew install git` on a Mac).

**Tell Git who you are** (this shows up on every commit):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**Create a GitHub account** at https://github.com if you don't have one.

**Set up authentication.** The easiest modern way is the GitHub CLI:

```bash
# Install: https://cli.github.com   (or: brew install gh)
gh auth login
```

Follow the prompts (choose *GitHub.com* → *HTTPS* → *login with a browser*).
This saves you from typing passwords/tokens later.

---

## 1. Get this project onto GitHub

You have a folder on your computer. Let's turn it into a GitHub repository.

### Step 1a — Make it a Git repository

From inside this `github-practice` folder:

```bash
git init
git add .
git commit -m "Initial commit: task tracker practice project"
```

What just happened:
- `git init` created a hidden `.git` folder — this is what makes it a *repository*.
- `git add .` **staged** all the files (marked them to be saved).
- `git commit` **saved a snapshot** of them, with a message describing it.

### Step 1b — Create the repository on GitHub and push

With the GitHub CLI, one command does it all:

```bash
gh repo create github-practice --public --source=. --push
```

That creates the repo on GitHub *and* uploads (`push`es) your commit.

> **No `gh`?** Create an empty repo on github.com (the **+** in the top-right →
> *New repository*, name it `github-practice`, **don't** add a README), then run
> the commands GitHub shows you — they'll look like:
> ```bash
> git remote add origin https://github.com/YOUR-USERNAME/github-practice.git
> git branch -M main
> git push -u origin main
> ```

🎉 Refresh the repo page on GitHub — your files are there!

---

## 2. The daily workflow: branches

**Never do your work directly on the `main` branch.** Instead, make a *branch*:
a parallel copy where you can experiment safely. If it goes wrong, you throw the
branch away and `main` is untouched.

Let's add a feature. We'll make the app able to **delete** a task.

### Step 2a — Create a branch and switch to it

```bash
git switch -c add-delete-command
```

`-c` means "create". You're now on the `add-delete-command` branch. Check anytime with:

```bash
git status        # tells you which branch you're on and what's changed
git branch        # lists all branches; * marks the current one
```

### Step 2b — Make your change

Open `src/tasks.py` and add a `delete` command. (Try it yourself! If you get
stuck, there's a worked solution at the bottom of this file.)

### Step 2c — See what you changed

```bash
git diff          # shows line-by-line what you edited
```

### Step 2d — Stage and commit

```bash
git add src/tasks.py
git commit -m "Add a delete command to remove tasks"
```

💡 **Good commit messages** describe *why* in the present tense: "Add delete
command", not "changed stuff".

### Step 2e — Push the branch to GitHub

```bash
git push -u origin add-delete-command
```

The `-u` links your local branch to the one on GitHub, so next time you can just
type `git push`.

---

## 3. Open a Pull Request (PR)

A pull request says: *"Here are my changes on this branch — please review and
merge them into `main`."* It's the heart of collaboration on GitHub.

```bash
gh pr create --fill
```

`--fill` uses your commit message as the PR title/description. Or open the repo
on github.com — you'll see a yellow banner offering to "Compare & pull request".

On the PR page you can:
- See exactly which lines changed (the **Files changed** tab).
- Leave comments on specific lines.
- Run through the checklist from our PR template.

---

## 4. Review and merge

In a real team, **someone else** reviews your PR. Since this is your practice
repo, you get to play both roles:

1. Open the PR on GitHub and click **Files changed**.
2. Click **Review changes** → leave a comment → choose **Approve**.
3. Go back to the **Conversation** tab and click **Merge pull request** →
   **Confirm merge**.
4. Click **Delete branch** (the branch did its job; tidy up).

Your feature is now part of `main`! 🎉

---

## 5. Sync your computer back up

GitHub's `main` now has the merged change, but your *local* `main` doesn't yet.
Bring it up to date:

```bash
git switch main
git pull
```

`git pull` downloads the latest `main` from GitHub. Now delete your finished
local branch:

```bash
git branch -d add-delete-command
```

You're back to a clean `main`, ready for the next feature. **This is the loop
that repeats forever:** branch → commit → push → PR → review → merge → pull.

---

## 6. Practicing "cloning"

You already have this repo locally, but cloning is how you'll download *other*
people's repos (or your own, onto a new machine). Try it in a different folder:

```bash
cd ..
git clone https://github.com/YOUR-USERNAME/github-practice.git github-practice-clone
cd github-practice-clone
```

`git clone` downloads the entire repository — all files and full history — and
sets up the `origin` link automatically. This is usually step one when you join
any project.

---

## Command cheat sheet

| Command | What it does |
|---|---|
| `git clone <url>` | Download a repo to your computer |
| `git status` | What branch am I on? What's changed? |
| `git switch -c <name>` | Create a new branch and switch to it |
| `git switch <name>` | Switch to an existing branch |
| `git add <file>` | Stage a change to be committed |
| `git add .` | Stage *all* changes |
| `git commit -m "msg"` | Save a snapshot of staged changes |
| `git diff` | See unstaged line-by-line changes |
| `git log --oneline` | See the history of commits |
| `git push` | Upload your commits to GitHub |
| `git pull` | Download the latest commits from GitHub |
| `git branch -d <name>` | Delete a finished local branch |
| `gh repo create` | Create a GitHub repo from the CLI |
| `gh pr create` | Open a pull request from the CLI |

---

## Worked solution for Step 2b (peek only if stuck!)

Add this function near the other ones in `src/tasks.py`:

```python
def delete_task(tasks, task_id):
    """Remove a task by id. Returns True if something was deleted."""
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return True
    return False
```

Then add a branch to the command handling in `main()`:

```python
    elif command == "delete":
        if len(argv) < 2:
            print("Please provide the task id, e.g. delete 1")
            return 1
        if delete_task(tasks, int(argv[1])):
            save_tasks(tasks)
            print(f"Deleted task #{argv[1]}")
        else:
            print(f"No task with id {argv[1]}")
            return 1
```

Bonus: add a test for it in `tests/test_tasks.py` and watch it pass before you
open your PR.
