document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('userInput');
    const chatBox = document.getElementById('chatBox');
    const sendBtn = document.getElementById('sendBtn');

    sendBtn.addEventListener('click', async () => {
        const userMessage = input.value;
        if (!userMessage) return;

        addMessage('You', userMessage);
        input.value = '';

        const response = await fetch('http://localhost:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();
        addMessage('Bot', data.reply);
    });

    function addMessage(sender, message) {
        const msg = document.createElement('div');
        msg.className = 'message';
        msg.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatBox.appendChild(msg);
    }
});
          
