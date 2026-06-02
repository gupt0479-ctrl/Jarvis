---
type: concept
course: Life
status: sprout
mastery (1/10): 4
created: 2026-01-15
topics:
  - "[[Cheat Sheet's & Notes]]"
  - "[[Ubuntu - WSL]]"
  - "[[40_Resources/CS/Links|Links]]"
  - "[[Winter Break]]"
related:
  - "[[40_Resources/CS/Links|Links]]"
---
# Git & GitHub
## MOC
### Used
- [[Arc (Learning Tracker)]]
- [[Portfolio]]
- 
## Definition
- Used to share your code amongst your fellow competitive coders.
### Quick dictionary: repo, branch, commit, push, staging
#### What is a _repo_?
A **repository (repo)** is:
- A project folder **+** the full history of all changes Git is tracking.
- On your machine: `~/projects/boom`
- On GitHub: `https://github.com/boom-astro/boom` (upstream) and  
    `https://github.com/gupta-builds/boom` (your fork)
Think: _one project, one repo_.
#### What is a _branch_?
A **branch** is a _line of development_ inside a repo.
- `main` → the “official” line of history.
- `feature/tracing-instrumentation` → your separate line where you’re doing tracing work.
Theo’s advice:
> [!NOTE] “never ever commit anything to the main branch of a fork… one branch = one PR ideally”

So:
- Keep `main` clean and in sync with upstream.
- Do your work on branches like `feature/tracing-instrumentation`.
- Each branch becomes one PR.
You **are** on your feature branch right now, which is what you want.
#### What does _staging_ mean?
Your `git status` shows:
```bash
Changes to be committed:      # ✅ already staged 
Changes not staged for commit # ❌ not staged yet 
Untracked files               # Git isn't tracking these yet
```
Think of it like this:
- **Working directory** = your actual files right now.
- **Staging area** = a “basket” of changes you are preparing for the next commit.
- **Commit** = a snapshot of whatever is in the staging area.
When you run: `git add src/api/routes/babamul.rs` you’re saying: “Include the current version of this file in my next commit.”. If you edit the file again after that, those _new_ edits are **not** in the staging area until you `git add` again.
#### What does _commit_ do?
`git commit -m "feat(tracing): add observability instrumentation across BOOM"`
- Takes **everything in the staging area** and stores a _snapshot_ of it in the repo’s history.
- It lives **only on your machine** at this moment.
- You can go back to that snapshot later, see the diff, etc.
- It does **not** send anything to GitHub.
Nothing “magical” happens to the files – you’re just recording their current state in history.
#### What does _push_ do?
`git push origin feature/tracing-instrumentation`
- Takes your local commits on this branch…
- …and sends them to the **remote repo** (`origin` → your fork).
- After this, GitHub sees your branch and you can open a PR.
> [!summary] So: **Stage → Commit → Push → PR**
## Why it matters
- If you can't share your code and have to do it manually to get work done. You are going to fuck up a lot of things so we need people to work for you, 
## Resources
- [[Cheat Sheet's & Notes#Git & GitHub|Git & GitHub Pdf]]
- 
## [[Cheat Sheet's & Notes#Git & GitHub|Git Commands pdf]]
### Initial Git Setup and Repository Creation
- Verify Git installation with `git --version`.
- Configure Git with your **name** and **email** for commit authorship tracking:
```bash
git config --global user.name 'Your Name' 
git config --global user.email 'your.email@example.com'
```
- `git init`: Initializes a new Git repository in the current folder, creating a `.git` hidden directory to start version tracking.
- Create files and check status with `git status` (shows untracked or changed files).
- Add files to be tracked with `git add <filename>` or `git add .` (to add all changes).
- Commit changes with descriptive messages using: `git commit -m "Your commit message"`.
	- When writing a commit message, *answer this question*: 
		- **If applied to the codebase then then commit will __ __ __ ? Remove filler words**.
### Commands
1. `git checkout <commit_hash>`: allows you to view the repository state at a specific commit, but this causes a **detached HEAD** state, where HEAD points to a past commit instead of the latest branch tip.
	- Detached HEAD is safe to explore but not for ongoing work; to resume normal work, checkout the branch again (`git checkout main`). It does **not delete any commit history or files**; it merely shows a snapshot.
2. `git checkout main`: Switches back to the `main` branch from any other branch or detached HEAD state.
3. `git checkout -f main`: Forcefully switches to the `main` branch, discarding any uncommitted changes.
4. `git log --oneline` — compact history view, `git log` — view commit history.
5. `git diff` — view line-by-line changes (working tree vs staged/repo)
6. `git branch <branch_name>`: Creates a new branch with the given name based on the current branch’s state but does not switch to it.
7. `git checkout <branch_name>`: Switches to the specified existing branch.
8.  `git checkout -b <branch_name>`: Creates a new branch and immediately switches to it in one command.
9. `git branch <new_branch_name> <source_branch_name>`: Creates a new branch based on the specified source branch without switching to it.
10.  `git push --set-upstream origin <branch_name>`: Pushes the local branch to the remote repository and sets the remote branch as the upstream tracking branch for easy future pushes.
11.  `git push -u origin <branch_name>`: Shortcut for `--set-upstream`; pushes and sets upstream tracking.
12.  `git push origin main`: Pushes the local `main` branch commits to the remote repository.
13. `git pull`: Fetches changes from the remote repository and merges them into the current local branch to synchronize.
14. `git branch -D <branch_name>`: Deletes a local branch forcefully.
15. `git merge <branch_name>`: Merges the specified branch into the current branch, combining their histories and changes.
16. `git reset --soft <commit_hash>`: Moves the current branch pointer to the specified commit but keeps all changes staged (ready to commit).
17. `git reset <commit_hash>` (mixed reset): Moves the current branch pointer to the specified commit, unstages changes but keeps them in the working directory.
18. `git reset --hard <commit_hash>`: Moves the current branch pointer to the specified commit and discards all changes in the working directory and staging area after that commit.
19. `git revert <commit_hash>`: Creates a new commit that undoes the changes introduced by the specified commit, preserving history.
20. `git stash`: Temporarily saves uncommitted changes (both staged and unstaged) to a stack so you can work on something else.
21. `git stash list`: Lists all saved stashes with their identifiers.30. `git stash apply stash@{0}`: Applies the changes saved in a specific stash to your working directory without removing the stash.
22.  `git remote add origin <repository_url>`: Adds a remote repository named `origin` pointing to the given URL, linking your local repo to a remote server like GitHub.
23. `git branch -m main`: Renames the current branch to `main`.
24. `git clone <repository_url>`: (Not explicitly shown but implied as background knowledge) Clones a remote repository to your local machine, creating a copy.
25. `git cherry-pick <commit_hash>`: Applies changes from a specific commit on another branch onto the current branch, selectively merging commits.
### Summary of Workflows and Concepts:
- **Branching:** Use `git branch` and `git checkout` to create and switch between branches for isolated development.
- **Committing:** Use `git add .` + `git commit` frequently to record changes.
- **Pushing/Pulling:** Use `git push` and `git pull` to sync local and remote repositories.
- **Merging:** Use `git merge` or GitHub Pull Requests to combine branches.
- **Undoing Changes:** Use `git reset` (soft, mixed, hard) and `git revert` depending on whether you want to rewrite history or keep it intact.
- **Stashing:** Use `git stash` to temporarily save changes when you need to switch tasks.
- **Remote Management:** Use `git remote add` to link remotes, and manage branches with upstream tracking.
## Common mistakes
- 
## Mini-test (answer without looking)
- [ ] Flashcards
- [ ] 
## Flashcards (best 3–8)
