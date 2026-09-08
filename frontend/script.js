// Get HTML elements
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatBox = document.getElementById("chat-box");


// --------------------------------------------------
// Function to add a message to the chat
// --------------------------------------------------

function addMessage(message, sender) {

    const messageElement = document.createElement("div");

    messageElement.classList.add("message");

    if (sender === "user") {
        messageElement.classList.add("user-message");
    } else {
        messageElement.classList.add("ai-message");
    }

    messageElement.textContent = message;

    chatBox.appendChild(messageElement);

    // Automatically scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}


// --------------------------------------------------
// Function to send message to FastAPI backend
// --------------------------------------------------

async function sendMessage() {

    // Get the text from the input box
    const message = messageInput.value.trim();

    // Don't send an empty message
    if (message === "") {
        return;
    }


    // Show user's message on the screen
    addMessage(message, "user");


    // Clear the input box
    messageInput.value = "";


    try {

        // Send message to FastAPI
        const response = await fetch("http://localhost:8000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        // Check if backend returned an error
        if (!response.ok) {

            throw new Error("Server error");

        }


        // Convert backend JSON response
        // into a JavaScript object
        const data = await response.json();

        console.log("Backend response:", data);
        console.log("data.response:", data.response);
        console.log("Type:", typeof data.response);

        addMessage(data.response, "ai");

    } catch (error) {

        console.error("Error:", error);

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "ai"
        );

    }

}


// --------------------------------------------------
// Send message when button is clicked
// --------------------------------------------------

sendButton.addEventListener("click", sendMessage);


// --------------------------------------------------
// Send message when Enter key is pressed
// --------------------------------------------------

messageInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});