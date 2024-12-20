// Seleccionar elementos del DOM
const messagesContainer = document.getElementById('messages');
const questionInput = document.getElementById('question-input');
const sendButton = document.getElementById('send-btn');

// Función para agregar mensajes al chat
function appendMessage(content, type) {
    const message = document.createElement('div');
    message.classList.add('message', type);
    message.textContent = content;
    messagesContainer.appendChild(message);
    messagesContainer.scrollTop = messagesContainer.scrollHeight; // Hacer scroll al final
}

// Función para enviar preguntas al backend
async function sendQuestion() {
    const questionText = questionInput.value.trim();

    if (!questionText) {
        alert("La pregunta no puede estar vacía.");
        return;
    }

    // Mostrar la pregunta en el chat
    appendMessage(questionText, 'question');
    questionInput.value = ''; // Limpiar el campo de texto

    try {
        const response = await fetch("http://localhost:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: questionText })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || "Error al procesar la solicitud.");
        }

        const data = await response.json();
        appendMessage(data.response, 'response'); // Mostrar la respuesta
    } catch (error) {
        appendMessage(`Error: ${error.message}`, 'response');
    }
}

// Agregar evento al botón de enviar
sendButton.addEventListener('click', sendQuestion);

// Agregar evento al presionar Enter en el campo de texto
questionInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendQuestion();
    }
});
