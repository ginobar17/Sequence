ROWS = 10
COLS = 10


def check_winner(board, player):

    # HORIZONTAL
    for row in range(ROWS):

        for col in range(COLS - 4):

            if all(board[row][col + i]["chip"] == player for i in range(5)):
                return True

    # VERTICAL
    for row in range(ROWS - 4):

        for col in range(COLS):

            if all(board[row + i][col]["chip"] == player for i in range(5)):
                return True

    # DIAGONAL \
    for row in range(ROWS - 4):

        for col in range(COLS - 4):

            if all(board[row + i][col + i]["chip"] == player for i in range(5)):
                return True

    # DIAGONAL /
    for row in range(4, ROWS):

        for col in range(COLS - 4):

            if all(board[row - i][col + i]["chip"] == player for i in range(5)):
                return True

    return False