class TicTacToe:
    def __init__(self):
        # Initialize the game board as a 2D list with empty strings
        self.board = [['' for _ in range(3)] for _ in range(3)]
        # Set the starting player as X
        self.current_player = 'X'

    def make_move(self, row, col):
        # Check if the cell is already occupied
        if self.board[row][col] != '':
            raise ValueError("This cell is already occupied")

        # Make the move and switch the current player
        self.board[row][col] = self.current_player
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_win(self):
        # Check rows and columns for wins
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return self.board[0][i]

        # Check diagonals for wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]

        # Check for draw
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    return None

        return 'D'

    def reset(self):
        # Reset the game board and current player
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
