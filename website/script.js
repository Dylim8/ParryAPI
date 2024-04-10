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
        applyThresholds();
    });
    // Listener for dark mode
    document.addEventListener('DOMContentLoaded', loadDarkModePreference);
});
document.addEventListener('DOMContentLoaded', function() {
    // Rest of your event listeners...

    // Event listener for dark mode toggle button
    const darkModeToggleButton = document.getElementById('darkModeToggle');
    if (darkModeToggleButton) {
        darkModeToggleButton.addEventListener('click', function() {
            toggleDarkMode();
            saveDarkModePreference();
        });
    }
});

// Function to handle simple sentiment analysis
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

// Initialize thresholds with default values
let positiveThreshold = 0.2;
let negativeThreshold = -0.2;

// Function to apply user-defined thresholds specifically for the chat
function applyChatThresholds() {
    positiveThreshold = parseFloat(document.getElementById('positiveThresholdChat').value) || 0.2;
    negativeThreshold = parseFloat(document.getElementById('negativeThresholdChat').value) || -0.2;
    console.log(`Chat thresholds updated. Positive: ${positiveThreshold}, Negative: ${negativeThreshold}`);
}

// Function to handle message sentiment analysis with custom thresholds
function analyzeMessageSentiment(message, callback) {
    const encodedMessage = encodeURIComponent(message);
    const url = `http://127.0.0.1:5500/parry/${encodedMessage}?posThreshold=${positiveThreshold}&negThreshold=${negativeThreshold}`;

    fetch(url)
    .then(response => response.json())
    .then(data => {
        // The API should classify sentiment based on the provided thresholds
        const compoundScore = data.compound; // Adjust if the score is nested differently
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
        callback(message, 'Error'); // Use 'Error' as sentiment in case of failure
    });
}

document.getElementById('applyThresholdsButton').addEventListener('click', applyThresholds);

// Function to handle sending chat messages
function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const messageText = messageInput.value.trim();
    if (messageText) {
        analyzeMessageSentiment(messageText, displayMessage); // Pass displayMessage as callback
        messageInput.value = ''; // Clear input after sending
    }
}

// Function to display messages in the chat area
function displayMessage(message, sentiment) {
    const chatArea = document.getElementById('chatArea');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    
    // Apply different class if the sentiment is Negative
    if (sentiment === 'Negative') {
        messageElement.classList.add('hidden-message');
        messageElement.textContent = message; // Set text content to message
        
        // Event listener to reveal message on click
        messageElement.addEventListener('click', function() {
            this.classList.remove('hidden-message');
            this.style.color = "#721c24"; // Optional: Change text color after revealing
        });
    } else {
        messageElement.textContent = `${message} (${sentiment})`; // Display message with sentiment for non-negative messages
    }

    chatArea.appendChild(messageElement);
    chatArea.scrollTop = chatArea.scrollHeight; // Auto-scroll to the newest message
}

// Function to toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    saveDarkModePreference();
}

// Function to save dark mode preference
function saveDarkModePreference() {
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode ? 'enabled' : 'disabled');
}

// Function to load dark mode preference
function loadDarkModePreference() {
    const darkMode = localStorage.getItem('darkMode');
    if (darkMode === 'enabled') {
        document.body.classList.add('dark-mode');
    }
}
