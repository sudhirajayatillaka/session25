# Git and pull request worksheet

Git records versions of your files. GitHub stores those versions online. A
pull request asks the instructor to review work from your fork.

## One-time setup

Open a VS Code terminal and replace the example values with your own:

```text
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

## Save your workshop work

First, ask Git what changed:

```text
git status
```

Add your workshop files to the next saved version:

```text
git add main.py static/index.html static/script.js static/styles.css
```

Create the saved version, called a commit:

```text
git commit -m "Complete web development challenges"
```

Send the commit to your GitHub fork:

```text
git push origin main
```

If your branch is not named `main`, `git status` displays its name. Use that
name in the push command instead.

## Open the pull request

1. Open your fork on GitHub.
2. Select **Contribute**, then **Open pull request**.
3. Check that the base repository is the instructor's repository and the head
   repository is your fork.
4. Use the title `Workshop submission - Your Name`.
5. Select **Create pull request**.
6. Wait for **Web Dev checks**. Open the check to see which level needs work.

When you fix something, repeat `git add`, `git commit`, and `git push`. The same
pull request updates automatically.

