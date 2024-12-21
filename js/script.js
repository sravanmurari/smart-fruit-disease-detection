document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    const result = await response.text();
    document.getElementById('result').innerHTML = result;
});

document.getElementById('yesButton').addEventListener('click', async () => {
    const className = document.querySelector('strong').innerText; // Get the predicted class name
    const response = await fetch(`/pesticides?class=${className}`);
    const recommendations = await response.json();
    const recommendationsDiv = document.getElementById('pesticideRecommendations');
    recommendationsDiv.innerHTML = `<strong>Pesticide Recommendations:</strong> ${recommendations.join(', ')}`;
    recommendationsDiv.style.display = 'block';
});

document.getElementById('noButton').addEventListener('click', () => {
    alert("No pesticide recommendations will be displayed.");
});
