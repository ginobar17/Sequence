ROWS = 10
COLS = 10

EMPTY = 0
PLAYER = 1
AI = 2


def create_board():

    board = []

    for row in range(ROWS):

        current_row = []

        for col in range(COLS):
            current_row.append(EMPTY)

        board.append(current_row)

    return board