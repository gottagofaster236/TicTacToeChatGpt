// JavaScript code to handle player moves
const cells = document.querySelectorAll("#game-board td");

cells.forEach((cell) => {
  cell.addEventListener("click", (event) => {
    // Make a move and send it to the server
    makeMove(event.target.id);
  });
});

function makeMove(cellId) {
  // Send a request to the server with the selected cell
  fetch("/make_move", {
    method: "POST",
    body: JSON.stringify({ cell: cellId }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      // Update the game board with the new move
      updateBoard(data);
    });
}

function updateBoard(data) {
  // Iterate over the board and update the cells with X or O
  for (let i = 0; i < data.board.length; i++) {
    for (let j = 0; j < data.board[i].length; j++) {
      const cellId = `cell-${i}-${j}`;
      const cell = document.querySelector(`#${cellId}`);
      cell.innerHTML = data.board[i][j];
      cell.classList.remove("x");
      cell.classList.remove("o");
      if (data.board[i][j] === "X") {
        cell.classList.add("x");
      } else if (data.board[i][j] === "O") {
        cell.classList.add("o");
      }
    }
  }

  // Update the current player display
  if (data.current_player) {
    document.querySelector("#current-player").textContent = `Current player: ${data.current_player}`;
  } else {
    // The game has ended, display a message to the user
    if (data.result == "X") {
      document.querySelector("#current-player").textContent = "X wins!";
    } else if (data.result == "O") {
      document.querySelector("#current-player").textContent = "O wins!";
    } else {
      document.querySelector("#current-player").textContent = "It's a draw!";
    }
  }
}

document.querySelector("#return-button").addEventListener("click", () => {
  window.location.href = "/";
});
