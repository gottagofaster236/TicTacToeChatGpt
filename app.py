from flask import Flask, request, jsonify, render_template
from tic_tac_toe import TicTacToe

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/game")
def game():
    # Pass data to the template
    data = {"board": game.board, "current_player": game.current_player}
    return render_template("game.html", **data)

game = TicTacToe()

@app.route("/make_move", methods=["POST"])
def make_move():
    # Get the cell from the request body
    cell = request.json["cell"]
    # Parse the cell id to get the row and column
    row, col = map(int, cell.split("-")[1:])
    # Make the move and check the result
    game.make_move(row, col)
    result = game.check_win()

    if result is None:
        # The game is still in progress
        return jsonify({"board": game.board, "current_player": game.current_player})
    elif result == "D":
        # The game is a draw
        game.reset()
        return jsonify({"board": game.board, "result": "D"})
    else:
        # A player has won the game
        game.reset()
        return jsonify({"board": game.board, "result": result})

if __name__ == "__main__":
    app.run()
