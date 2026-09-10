// Level 2: Find the name input, button, and output with document.querySelector.
// Add a click event listener that displays: Hello, NAME!
const inputField = document.querySelector("input");
const greetBtn = document.querySelector("button");
const outputField = document.querySelector(".message")

greetBtn.addEventListener("click", () => {
    namestr = inputField.value;
    greetstr = "Hello " + namestr + "!"
    outputField.innerText = greetstr
});

// Level 3: Listen for the login form's submit event.
// Prevent the page refresh, read both inputs, and show an error when either is blank.
// Use the CSS classes "success" and "error" on #login-message.


// Level 4: When #hello-button is clicked, fetch GET /hello and display its message.

// Level 5: Replace the Level 3 success-only behavior with fetch POST /login.
// Send JSON with username and password, then display the backend message.
