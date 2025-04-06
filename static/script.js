document.addEventListener('DOMContentLoaded', function() { // Ensure DOM is loaded

    const messageArea = document.getElementById('messageArea');
    const textInput = document.getElementById('text');
    const messageBox = document.getElementById('messageFormeight');

    // --- Function to add a message to the chat window ---
    function addMessage(sender, text, time) {
        let messageHtml = '';
        const escapedText = escapeHtml(text); // Escape text before inserting

        if (sender === 'user') {
            messageHtml = `
                <div class="message-row sent">
                    <div class="msg_cotainer_base msg_cotainer_send">
                        ${escapedText}
                        <span class="msg_time_base msg_time_send">${time}</span>
                    </div>
                    <div class="img_cont_msg">
                        <img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="user_img_msg">
                    </div>
                </div>`;
        } else if (sender === 'bot') {
             messageHtml = `
                <div class="message-row received">
                    <div class="img_cont_msg">
                         <img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="user_img_msg">
                    </div>
                    <div class="msg_cotainer_base msg_cotainer">
                        ${escapedText}
                        <span class="msg_time_base msg_time">${time}</span>
                    </div>
                </div>`;
        } else if (sender === 'error') {
             messageHtml = `
                <div class="message-row received">
                    <div class="img_cont_msg">
                         <img src="https://static.vecteezy.com/system/resources/previews/016/017/018/non_2x/ecommerce-icon-free-png.png" class="user_img_msg">
                    </div>
                    <div class="msg_cotainer_base msg_cotainer" style="background-color: #dc3545; border-color: #dc3545;"> ${escapedText}
                        <span class="msg_time_base msg_time">${time}</span>
                    </div>
                </div>`;
        }

        if (messageHtml) {
            messageBox.insertAdjacentHTML('beforeend', messageHtml);
            scrollToBottom(); // Scroll down after adding message
        }
    }

    // --- Event listener for form submission ---
    messageArea.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const date = new Date();
        const minute = date.getMinutes().toString().padStart(2, '0');
        const hour = date.getHours();
        const str_time = hour + ":" + minute;
        const rawText = textInput.value.trim();

        if (rawText === "") {
            return; // Don't send empty messages
        }

        // Display user's message immediately
        addMessage('user', rawText, str_time);

        // Clear the input field
        textInput.value = "";

        // --- Send message to the backend using Fetch API ---
        fetch("/get", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({ 'msg': rawText })
        })
        .then(response => {
            if (!response.ok) {
                // If response status is not OK, try to read error text, otherwise throw generic error
                 return response.text().then(text => {
                    throw new Error(`HTTP error! status: ${response.status}, message: ${text || 'Server error'}`);
                 });
            }
            return response.text(); // Expect plain text response
        })
        .then(data => {
            // Display bot's response
             addMessage('bot', data, str_time);
        })
        .catch(error => {
            console.error('Error fetching bot response:', error);
            // Display a user-friendly error message in the chat
            addMessage('error', `Sorry, something went wrong. (${error.message})`, str_time);
        });
    });

    // --- Function to scroll the message box to the bottom ---
    function scrollToBottom() {
        // Using setTimeout helps ensure the scroll happens after the DOM update
        setTimeout(() => {
             messageBox.scrollTop = messageBox.scrollHeight;
        }, 0);
    }

    // --- Simple HTML escaping function to prevent XSS ---
    function escapeHtml(unsafe) {
        if (typeof unsafe !== 'string') return unsafe;
        return unsafe
             .replace(/&/g, "&amp;")
             .replace(/</g, "&lt;")
             .replace(/>/g, "&gt;")
             .replace(/"/g, "&quot;")
             .replace(/'/g, "&#039;");
     }

     // --- Initial scroll to bottom ---
     // Useful if there are predefined messages or if loading chat history
     scrollToBottom();

     // --- Focus the input field on load ---
     textInput.focus();

});