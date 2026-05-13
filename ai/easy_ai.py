import random


def get_move(board):

    empty_cells = []

    for row in range(10):

        for col in range(10):

            if board[row][col] == 0:
                empty_cells.append((row, col))

    if empty_cells:
        return random.choice(empty_cells)

    return None