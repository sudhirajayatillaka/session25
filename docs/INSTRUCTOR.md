# Instructor guide

## Before publishing

1. Replace `@YOUR_GITHUB_USERNAME` in `.github/CODEOWNERS` with the instructor
   or teaching-team owner.
2. Configure a main-branch ruleset that requires pull requests, Code Owner
   review for grading infrastructure, and the `Web Dev checks` status.
3. Run the clean-machine rehearsal on Windows 11.
4. Keep the completed solution in a private instructor repository or a branch
   that is not included in student forks.
5. Expect GitHub to ask a maintainer to approve the first workflow run from
   some first-time fork contributors; approve it from the pull request page.

Do not use `pull_request_target` to execute submissions. The provided workflow
uses a read-only `pull_request` job, checks out the submission separately, and
runs grader files from the upstream base commit.

## Suggested schedule

### Separate 45–60 minute preparation block

- Install Python 3.12, Git, and VS Code.
- Create/sign in to GitHub accounts.
- Configure Git name and email.
- Fork and HTTPS-clone the repository.
- Run `setup.bat` and `check.bat 1`.

Have the dependency and Chromium downloads cached on the venue network if
internet access is limited. Pair students while resolving installation issues.

### 105-minute coding block

- 0–15: open the running app and explain the four technology roles.
- 15–35: complete Level 2 and rerun its check.
- 35–55: complete Level 3 and discuss browser-side validation.
- 55–80: complete Level 4 and inspect the request in browser developer tools.
- 80–105: complete Level 5 and compare successful and unsuccessful responses.

Teach the PR commands in a short wrap-up after the coding block.

## Teaching notes

- Ask students to run only their current level so future failures do not create
  noise. Run `check.bat all` at the end.
- Explain the Network tab before introducing `fetch`.
- Keep the frontend and API on one origin; CORS is intentionally outside scope.
- Tests check behaviour and stable element IDs. CSS appearance and exact source
  structure are not graded.
- The starter passes Level 1 and fails Levels 2–5 by design.

## Reference solution behaviour

The instructor solution must preserve every earlier checkpoint. Its form
handler should validate blanks first, send JSON only for completed fields, read
both successful and error JSON responses, and apply `success` or `error` to the
message element. Network errors should show `Something went wrong. Try again.`
