document.addEventListener('DOMContentLoaded', function() {
    // Event listener for the "Analyze Text" button
    document.getElementById('analyzeButton').addEventListener('click', function(e) {
        analyzeText();
    });

    // Event listener for pressing Enter in the chat message input
    document.getElementById('messageInput').addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Prevent the default action to avoid new line in textarea
            sendMessage();
        }
    });

    // Event listener for the "Apply Thresholds" button
    document.getElementById('applyThresholdsButton').addEventListener('click', function() {
        applyChatThresholds(); // Make sure the function name matches the defined function
    });

    // Load dark mode preferences on page load
    loadDarkModePreference();

    const darkModeToggleButton = document.getElementById('darkModeToggle');
    if (darkModeToggleButton) {
    darkModeToggleButton.addEventListener('click', function() {
        toggleDarkMode();
        saveDarkModePreference();
    });
    } else {
        console.log('Dark mode toggle button not found');
    }
});

function analyzeText() {
    const userInput = encodeURIComponent(document.getElementById('userInput').value);
    const url = `http://127.0.0.1:5500/parry/${userInput}`;
    
    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Analysis result:', data);
        document.getElementById('analysisResult').innerText = `Analysis result: ${JSON.stringify(data)}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('analysisResult').innerText = 'Failed to analyze text.';
    });
}

function applyChatThresholds() {
    positiveThreshold = parseFloat(document.getElementById('positiveThresholdChat').value) || 0.2;
    negativeThreshold = parseFloat(document.getElementById('negativeThresholdChat').value) || -0.2;
    console.log(`Chat thresholds updated. Positive: ${positiveThreshold}, Negative: ${negativeThreshold}`);
}

function analyzeMessageSentiment(message, callback) {
    const encodedMessage = encodeURIComponent(message);
    const url = `http://127.0.0.1:5500/parry/${encodedMessage}?posThreshold=${positiveThreshold}&negThreshold=${negativeThreshold}`;

    fetch(url)
    .then(response => response.json())
    .then(data => {
        const compoundScore = data.compound;
        let sentiment;
        if (compoundScore <= negativeThreshold) {
            sentiment = 'Negative';
        } else if (compoundScore >= positiveThreshold) {
            sentiment = 'Positive';
        } else {
            sentiment = 'Neutral';
        }

        callback(message, sentiment);
    })
    .catch(error => {
        console.error('Error analyzing sentiment:', error);
        callback(message, 'Error');
    });
}

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const messageText = messageInput.value.trim();
    if (messageText) {
        analyzeMessageSentiment(messageText, displayMessage);
        messageInput.value = '';
    }
}

function displayMessage(message, sentiment) {
    const chatArea = document.getElementById('chatArea');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    if (sentiment === 'Negative') {
        messageElement.classList.add('hidden-message');
        messageElement.textContent = message;
        messageElement.addEventListener('click', function() {
            this.classList.remove('hidden-message');
            this.style.color = "#721c24";
        });
    } else {
        messageElement.textContent = `${message} (${sentiment})`;
    }

    chatArea.appendChild(messageElement);
    chatArea.scrollTop = chatArea.scrollHeight;
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    saveDarkModePreference();
}

function saveDarkModePreference() {
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode ? 'enabled' : 'disabled');
}

function loadDarkModePreference() {
    const darkMode = localStorage.getItem('darkMode');
    if (darkMode === 'enabled') {
        document.body.classList.add('dark-mode');
    }
}
