document.getElementById("analyzeBtn").onclick = function() {
    const text = document.getElementById("inputText").value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = `
            <p>Predicted Emotion: ${data.emotion}</p>
            <img src="${data.icon_url}" alt="${data.emotion}" style="width: 100px; height: 100px;">
        `;
    })
    .catch(error => console.error('Error:', error));
};
