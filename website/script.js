// Set up the event listener for the Enter key
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('userInput').addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Prevent the default action to avoid line breaks in textarea
            analyzeText(); // Call the analyzeText function
        }
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('analyzeButton').addEventListener('click', function(e) {
        analyzeText();
    });
});

//analyze text button
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