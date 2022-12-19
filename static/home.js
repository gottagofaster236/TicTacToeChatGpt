document.addEventListener("DOMContentLoaded", () => {
  // Get the start button
  const startButton = document.getElementById("start-button");

  // Add a click event listener to the start button
  startButton.addEventListener("click", () => {
    // Navigate to the game page
    window.location.href = "/game";
  });
});
