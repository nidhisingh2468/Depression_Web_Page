// calculateResult.js
function calculateResult() {
    var totalScore = 0;

    // Calculate the total score for the first 9 questions
    for (var i = 1; i <= 9; i++) {
        var questionValue = parseInt(document.querySelector('input[name="question' + i + '"]:checked').value);
        totalScore += questionValue;
    }

    var resultElement = document.getElementById('result');
    resultElement.innerHTML = "Your total score is: " + totalScore;
}
