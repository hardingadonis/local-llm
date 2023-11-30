function sendMessage() {
    let userInput = document.getElementById("user-input").value;

    if (userInput === "") {
        return;
    }

    let messageElement = document.createElement("div");
    messageElement.classList.add("message");
    messageElement.classList.add("p-1");
    messageElement.innerHTML = `<strong class="p-1">You:</strong> <span class="p-3">${userInput}</span>`;

    document.getElementById("chat-container").appendChild(messageElement);

    document.getElementById("user-input").value = "";
}