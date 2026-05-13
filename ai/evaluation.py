PLAYER = 1
AI = 2

ROWS = 10
COLS = 10


def evaluate_board(board):

    score = 0

    # Horizontal
    for row in range(ROWS):

        for col in range(COLS - 4):

            window = []

            for i in range(5):
                window.append(board[row][col + i]["chip"])

            score += evaluate_window(window)

    # Vertical
    for row in range(ROWS - 4):

        for col in range(COLS):

            window = []

            for i in range(5):
                window.append(board[row + i][col]["chip"])

            score += evaluate_window(window)

    # Diagonal \
    for row in range(ROWS - 4):

        for col in range(COLS - 4):

            window = []

            for i in range(5):
                window.append(board[row + i][col + i]["chip"])

            score += evaluate_window(window)

    # Diagonal /
    for row in range(4, ROWS):

        for col in range(COLS - 4):

            window = []

            for i in range(5):
                window.append(board[row - i][col + i]["chip"])

            score += evaluate_window(window)

    return score


def evaluate_window(window):

    score = 0

    ai_count = window.count(AI)

    player_count = window.count(PLAYER)

    empty_count = window.count(0)

    # AI patterns
    if ai_count == 5:
        score += 100

    elif ai_count == 4 and empty_count == 1:
        score += 20

    elif ai_count == 3 and empty_count == 2:
        score += 8

    elif ai_count == 2 and empty_count == 3:
        score += 3

    # Player patterns
    if player_count == 5:
        score -= 100

    elif player_count == 4 and empty_count == 1:
        score -= 25

    elif player_count == 3 and empty_count == 2:
        score -= 10

    elif player_count == 2 and empty_count == 3:
        score -= 4

    return score