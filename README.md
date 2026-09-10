# Web Development First Steps

This workshop shows how HTML, CSS, JavaScript, and FastAPI work together. You
will make one small change at a time and run a checkpoint after each change.

## Before the coding session

Your instructor will guide you through these steps in a separate setup block:

1. Install **Python 3.12**, **Git**, and **Visual Studio Code**.
2. Create or sign in to a GitHub account.
3. Fork the workshop repository on GitHub.
4. Copy your fork's HTTPS URL and run:

   ```text
   git clone YOUR_FORK_URL
   cd REPOSITORY_NAME
   code .
   ```

5. Double-click `setup.bat`. The first setup downloads a test browser and may
   take several minutes.
6. Run `check.bat 1`. The starter should pass Level 1.

If double-clicking closes the window before you can read an error, open the
folder in VS Code, select **Terminal → New Terminal**, and type `setup.bat`.

## The four technologies

- **HTML** gives the page its elements and meaning.
- **CSS** controls how those elements look.
- **JavaScript** reacts to clicks, reads inputs, and calls the backend.
- **FastAPI** runs Python on the server and responds to browser requests.

## How to find answers during the workshop

The goal is to practise reading documentation and turning an example into your
own code. Please do not use an AI/LLM to generate solutions for these
challenges. For each level:

1. Read the short resources linked under that level.
2. Find the example closest to the task.
3. Type and adapt the code yourself instead of copying a complete solution.
4. Run the checkpoint and use its first error as your next clue.
5. If you are still stuck, ask a classmate or instructor and show what you
   already tried.

You do not need to understand every section of a linked page. Read the
introduction, study the relevant example, and return to the workshop task.

## Workshop checkpoints

### Level 1 - Setup (0–15 minutes)

Run `check.bat 1`. This should already pass. Start the app with `start.bat`,
then open <http://127.0.0.1:8000>.

Read:

- [MDN: Adding interactivity with JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)
- [FastAPI: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

### Level 2 - HTML + JavaScript (15–35 minutes)

Open `static/script.js`. Connect the name input and button so entering `Ada`
and clicking **Show greeting** displays a greeting containing `Ada`.

Read these sections for `querySelector`, `addEventListener`, input values, and
changing page text:

- [MDN: Introduction to events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events)
- [MDN: DOM scripting](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)

Run:

```text
check.bat 2
```

### Level 3 - Form validation (35–55 minutes)

Handle the login form's `submit` event. Prevent the normal page refresh. When
either field is blank, show a non-empty message in `#login-message`, add the
class `error`, and do not contact the backend. When both fields are present,
show a non-empty message with the class `success`.

Read:

- [MDN: Forms and buttons in HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_forms)
- [MDN: Client-side form validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)

Run `check.bat 3`.

### Level 4 - Connect to FastAPI (55–80 minutes)

In `main.py`, add:

```text
GET /hello → {"message": "Hello from FastAPI!"}
```

In `static/script.js`, use `fetch("/hello")` when the hello button is clicked
and display the returned message in `#hello-output`.

Read the basic GET route example and the first Fetch example:

- [FastAPI: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [MDN: Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

Run `check.bat 4`.

### Level 5 - Send login data (80–105 minutes)

Create a Pydantic request model and add this API contract:

```text
POST /login
JSON body: {"username": "...", "password": "..."}

student / webdev123 → 200, {"success": true, "message": "Login successful"}
anything else        → 401, {"detail": "Invalid username or password"}
```

Update the form handler to call `/login` with `fetch()`. Include the
`Content-Type: application/json` header and use `JSON.stringify`. Display a
successful response with the class `success`, and an unsuccessful response
with the class `error`.

Read:

- [FastAPI: Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI: Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [MDN: Using Fetch - setting a method, JSON body, and headers](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#making_a_request)

Run `check.bat 5`, then `check.bat all`.

> This is a learning demonstration, not real authentication. Production apps
> must not hardcode or store plaintext passwords and need secure sessions or
> tokens.

## Submitting your work

Follow [the Git worksheet](docs/GIT-WORKSHEET.md). Your pull request will run
the same five checkpoints. A green **Web Dev checks** result means they all
passed.

For extra guidance, read [GitHub's About Git introduction](https://docs.github.com/en/get-started/using-git/about-git)
and [Pull request quickstart](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart).

## When a check fails

Read the first failure, change one thing, save, and run the same checkpoint
again. Browser screenshots and traces are saved under `test-results` for an
instructor to inspect. You are not graded on styling or on writing the same
code as somebody else; only the documented behaviour is checked.
