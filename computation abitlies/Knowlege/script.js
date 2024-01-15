// script.js
document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input');
    const userText = userInput.value.trim();

    if(userText !== "") {
        addMessageToUI(userText, "user-message");
        userInput.value = "";
        getBotResponse(userText);
    }
});

function addMessageToUI(message, className) {
    const messagesDiv = document.getElementById('messages');
    const messageElement = document.createElement('li');
    messageElement.classList.add('message', className);
    messageElement.textContent = message;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function getBotResponse(userText) {
    // Simulate a bot response (Here you can integrate your chatbot backend)
    setTimeout(() => {
        addMessageToUI("This is a bot response to: " + userText, "bot-message");
    }, 1000);
}
