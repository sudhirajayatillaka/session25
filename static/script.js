// Level 2: Find the name input, button, and output with document.querySelector.
// Add a click event listener that displays: Hello, NAME!
const inputField = document.querySelector("input");
const greetBtn = document.querySelector("button");
const outputField = document.querySelector(".message");

greetBtn.addEventListener("click", () => {
    namestr = inputField.value;
    greetstr = "Hello " + namestr + "!";
    outputField.innerText = greetstr;
});

// Level 3: Listen for the login form's submit event.
// Prevent the page refresh, read both inputs, and show an error when either is blank.
// Use the CSS classes "success" and "error" on #login-message.
const loginForm = document.getElementById("login-form");
const nameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const loginMessage = document.getElementById("login-message")

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    if ((nameInput.value == "") || (passwordInput.value == "")) {
        loginMessage.innerText = "Error";
        if (loginMessage.classList.contains("success")) {
            loginMessage.classList.remove("success");
        }
        loginMessage.classList.add("error");
    } else {
        loginMessage.innerText = "Success";
        if (loginMessage.classList.contains("error")) {
            loginMessage.classList.remove("error");
        }
        loginMessage.classList.add("success");

    }
});

// Level 4: When #hello-button is clicked, fetch GET /hello and display its message.
const helloButton = document.getElementById("hello-button");
const helloOut = document.getElementById("hello-output");

async function GetData() {
    const Url = "http://127.0.0.1:8000/hello";
    try {
        const response = await fetch(Url);
        if (response.ok) {
            const datajson = await response.json();
            const messageData = datajson.message;
            helloOut.innerText = messageData;
        }
    } catch (e) {
        console.log(e);
    }
}

helloButton.addEventListener("click", () => {
    GetData();
})
// Level 5: Replace the Level 3 success-only behavior with fetch POST /login.
// Send JSON with username and password, then display the backend message.
