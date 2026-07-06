# The Hands-On GitHub Tutorial 🚀

This walks you through the **core GitHub workflow** using this very repository:
clone → branch → commit → push → pull request → review → merge.

Every step is shown **two ways**:

- 💻 **Terminal** — the Git commands. Great for understanding what's really happening.
- 🖱️ **VS Code** — the same thing with clickable buttons and panels.

They do the *exact same thing* under the hood — pick whichever you like, or do
both to connect the two in your head. Take it slowly; the muscle memory is the point.

> **The two icons you'll use most in VS Code:**
> - **Source Control** — the branching icon in the left sidebar (looks like a fork
>   in a road), or press `Ctrl/Cmd + Shift + G`. This is your home base for staging,
>   committing, and pushing.
> - **The status bar**, bottom-left corner — shows your current **branch name** and
>   sync arrows. Clickable.

---

## 0. One-time setup

**Install Git** (check if you already have it):

- 💻 **Terminal:**
  ```bash
  git --version
  ```
  If that errors, install it from https://git-scm.com/downloads (or `brew install git` on a Mac).
- 🖱️ **VS Code:** if Git isn't installed, the Source Control panel shows a
  **"Download Git"** button — click it and follow the installer, then restart VS Code.

**Tell Git who you are** (this shows up on every commit):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

> This one has no VS Code button — run it once in the terminal (open one inside VS
> Code with `` Ctrl/Cmd + ` ``) and you're set forever.

**Create a GitHub account** at https://github.com if you don't have one.

**Set up authentication** so you can push without typing passwords/tokens:

- 💻 **Terminal** — the GitHub CLI is the easiest:
  ```bash
  # Install: https://cli.github.com   (or: brew install gh)
  gh auth login
  ```
  Follow the prompts (choose *GitHub.com* → *HTTPS* → *login with a browser*).
- 🖱️ **VS Code:** click the **Accounts** icon (the little person, bottom-left of the
  sidebar) → **Sign in with GitHub**. A browser opens; approve, and VS Code is
  authenticated. Installing the **GitHub Pull Requests** extension (Extensions panel,
  search "GitHub Pull Requests") unlocks the PR features used later in this tutorial.

---

## 1. Get this project onto GitHub

You have a folder on your computer. Let's turn it into a GitHub repository.

### Step 1a — Make it a Git repository

From inside this `github-practice` folder:

- 💻 **Terminal:**
  ```bash
  git init
  git add .
  git commit -m "Initial commit: task tracker practice project"
  ```
- 🖱️ **VS Code:** open the **Source Control** panel → click **Initialize
  Repository**. Then to make the first commit: hover the **Changes** header and
  click the **+** (stages everything — same as `git add .`), type a message like
  `Initial commit: task tracker practice project` in the box at the top, and click
  the **✓ Commit** button.

What just happened:
- `git init` created a hidden `.git` folder — this is what makes it a *repository*.
- `git add` / the **+** **staged** the files (marked them to be saved).
- `git commit` / the **✓** **saved a snapshot** of them, with a message describing it.

### Step 1b — Create the repository on GitHub and push

- 🖱️ **VS Code (easiest):** after your first commit, the Source Control panel shows a
  blue **Publish Branch** button. Click it → choose **Publish to GitHub public
  repository**. VS Code creates the repo on GitHub *and* uploads it in one click.
- 💻 **Terminal** — with the GitHub CLI, one command does it all:
  ```bash
  gh repo create github-practice --public --source=. --push
  ```
  > **No `gh`?** Create an empty repo on github.com (the **+** in the top-right →
  > *New repository*, name it `github-practice`, **don't** add a README), then run:
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

- 💻 **Terminal:**
  ```bash
  git switch -c add-delete-command
  ```
  `-c` means "create". Check where you are anytime with `git status` (branch + what's
  changed) or `git branch` (lists branches; `*` marks the current one).
- 🖱️ **VS Code:** click the **branch name** in the bottom-left status bar → choose
  **+ Create new branch**, type `add-delete-command`, press Enter. The status bar now
  shows your new branch name — that's your "you are here."

### Step 2b — Make your change

Open `src/tasks.py` and add a `delete` command. (Try it yourself! If you get
stuck, there's a worked solution at the bottom of this file.)

> 🖱️ In VS Code, files you've edited turn **orange** in the Explorer and get an **M**
> ("modified") next to them. New files show up **green** with a **U** ("untracked").

### Step 2c — See what you changed

- 💻 **Terminal:**
  ```bash
  git diff          # shows line-by-line what you edited
  ```
- 🖱️ **VS Code:** click the file under **Changes** in the Source Control panel. A
  side-by-side **diff** opens — old version on the left, your version on the right,
  changes highlighted. (You'll also see colored bars in the editor's left margin as
  you type: green = added lines, blue = changed.)

### Step 2d — Stage and commit

- 💻 **Terminal:**
  ```bash
  git add src/tasks.py
  git commit -m "Add a delete command to remove tasks"
  ```
- 🖱️ **VS Code:** in Source Control, hover the file and click its **+** to **stage**
  it (moves it to a **Staged Changes** section). Type your message in the box —
  `Add a delete command to remove tasks` — and click **✓ Commit**.

💡 **Good commit messages** describe *why* in the present tense: "Add delete
command", not "changed stuff".

### Step 2e — Push the branch to GitHub

- 💻 **Terminal:**
  ```bash
  git push -u origin add-delete-command
  ```
  The `-u` links your local branch to the one on GitHub, so next time it's just `git push`.
- 🖱️ **VS Code:** click **Publish Branch** (or the **sync arrows** ↻ in the status
  bar). Because this branch is brand new, VS Code offers to publish it to GitHub —
  same as `git push -u`.

---

## 3. Open a Pull Request (PR)

A pull request says: *"Here are my changes on this branch — please review and
merge them into `main`."* It's the heart of collaboration on GitHub.

- 🖱️ **VS Code** (needs the **GitHub Pull Requests** extension from step 0): open its
  panel from the left sidebar → **Create Pull Request**. Fill in the title/description,
  confirm the branches (from `add-delete-command` into `main`), and click **Create**.
  You can review and even merge it without leaving the editor.
- 💻 **Terminal:**
  ```bash
  gh pr create --fill
  ```
  `--fill` uses your commit message as the PR title/description. (Or open the repo on
  github.com — you'll see a yellow banner offering to "Compare & pull request".)

On the PR page (in the browser *or* the VS Code panel) you can:
- See exactly which lines changed (the **Files changed** tab).
- Leave comments on specific lines.
- Run through the checklist from our PR template.

---

## 4. Review and merge

In a real team, **someone else** reviews your PR. Since this is your practice
repo, you get to play both roles.

- 🖱️ **In the browser (github.com):**
  1. Open the PR and click **Files changed**.
  2. Click **Review changes** → leave a comment → choose **Approve**.
  3. Back on the **Conversation** tab, click **Merge pull request** → **Confirm merge**.
  4. Click **Delete branch** (it did its job; tidy up).
- 🖱️ **In VS Code:** open the PR from the GitHub Pull Requests panel. You'll see the
  same **Files Changed**, a **Merge** button, and a checkbox to **delete the branch
  after merging**. Everything the website offers, in the editor.

Your feature is now part of `main`! 🎉

---

## 5. Sync your computer back up

GitHub's `main` now has the merged change, but your *local* `main` doesn't yet.

- 💻 **Terminal:**
  ```bash
  git switch main
  git pull
  git branch -d add-delete-command   # delete the finished local branch
  ```
- 🖱️ **VS Code:** click the **branch name** in the status bar → pick **main** to
  switch. Then click the **sync arrows** ↻ (or **⋯** menu → **Pull**) to download the
  merged change. To delete the old branch: **⋯** menu → **Branch** → **Delete
  Branch** → pick `add-delete-command`.

You're back to a clean `main`, ready for the next feature. **This is the loop that
repeats forever:** branch → commit → push → PR → review → merge → pull.

---

## 6. Practicing "cloning"

You already have this repo locally, but cloning is how you'll download *other*
people's repos (or your own, onto a new machine). Try it in a different folder:

- 💻 **Terminal:**
  ```bash
  cd ..
  git clone https://github.com/YOUR-USERNAME/github-practice.git github-practice-clone
  cd github-practice-clone
  ```
- 🖱️ **VS Code:** open the Command Palette (`Ctrl/Cmd + Shift + P`) → type
  **Git: Clone** → paste the repo URL → pick a folder. VS Code offers to open the
  cloned repo in a new window.

`git clone` downloads the entire repository — all files and full history — and
sets up the `origin` link automatically. This is usually step one when you join
any project.

---

## Terminal ⇄ VS Code cheat sheet

| Task | 💻 Terminal | 🖱️ VS Code |
|---|---|---|
| Download a repo | `git clone <url>` | Command Palette → **Git: Clone** |
| What branch / what changed? | `git status` | Source Control panel + status bar |
| Create & switch branch | `git switch -c <name>` | Status bar branch name → **Create new branch** |
| Switch branch | `git switch <name>` | Status bar branch name → pick it |
| Stage a change | `git add <file>` | **+** next to the file |
| Stage everything | `git add .` | **+** on the **Changes** header |
| Commit | `git commit -m "msg"` | Type message → **✓ Commit** |
| See line-by-line changes | `git diff` | Click a file in Source Control (opens a diff) |
| See commit history | `git log --oneline` | Command Palette → **Git: View History** (or the *Git Graph* extension) |
| Push | `git push` | **Sync** ↻ / **Publish Branch** |
| Pull | `git pull` | **Sync** ↻ / **⋯** → **Pull** |
| Delete a local branch | `git branch -d <name>` | **⋯** → **Branch** → **Delete Branch** |
| Create a GitHub repo | `gh repo create` | **Publish Branch** → *Publish to GitHub* |
| Open a pull request | `gh pr create` | GitHub Pull Requests panel → **Create Pull Request** |

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
