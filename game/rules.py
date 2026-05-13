ROWS = 10
COLS = 10


def check_winner(board, player):

    # Horizontal check
    for row in range(ROWS):

        for col in range(COLS - 4):

            if all(board[row][col + i] == player for i in range(5)):
                return True

    # Vertical check
    for row in range(ROWS - 4):

        for col in range(COLS):

            if all(board[row + i][col] == player for i in range(5)):
                return True

    # Diagonal (top-left to bottom-right)
    for row in range(ROWS - 4):

        for col in range(COLS - 4):

            if all(board[row + i][col + i] == player for i in range(5)):
                return True

    # Diagonal (bottom-left to top-right)
    for row in range(4, ROWS):

        for col in range(COLS - 4):

            if all(board[row - i][col + i] == player for i in range(5)):
                return True

    return False