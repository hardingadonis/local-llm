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


const userInput = document.getElementById('user-input');
const chatContainer = document.getElementById('chat-container');

const BOT_ENDPOINT = 'http://localhost:8000/v1';

const messages = [{
    role: 'system',
    content: "Answer short and concise in 200 tokens only."
}];

function renderMessages() {
    chatContainer.innerHTML = '';

    messages.forEach(message => {
        const messageElement = document.createElement('div');
        messageElement.className = messageClasses(message.role);
        messageElement.innerHTML = message.role === 'user' ? `<strong class="p-1">You:</strong> <span class="p-3">${message.content}</span>` : `<strong class="p-1">Local LLM:</strong> <span class="p-3">${message.content}</span>`;
        chatContainer.appendChild(messageElement);
    });
}

function messageClasses(role) {
    return 'text-start justify-content-start';
}

async function sendMessage() {
    if (!userInput.value.trim()) return;

    messages.push({
        role: 'user',
        content: userInput.value
    });

    renderMessages();

    try {
        userInput.value = '';

        const response = await fetch(`${BOT_ENDPOINT}/chat/completions`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                messages: messages,
                temperature: 0.9,
                max_tokens: 200,
            }),
        });

        const responseData = await response.json();

        messages.push({
            role: 'assistant',
            content: responseData.choices[0].message.content
        });

        renderMessages();
    } catch (error) {
        console.error('There was an error with the API request', error);
    }
}