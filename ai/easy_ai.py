import random


def get_move(board, ai_hand):

    possible_moves = []

    for row in range(10):

        for col in range(10):

            board_card = board[row][col]["card"]

            board_chip = board[row][col]["chip"]

            if (
                    board_chip == 0 and
                    (
                            board_card in ai_hand
                            or
                            any(card.startswith("J") for card in ai_hand)
                    )
            ):

                possible_moves.append((row, col, board_card))

    if possible_moves:
        return random.choice(possible_moves)

    return None