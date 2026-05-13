from ai.evaluation import evaluate_board

PLAYER = 1
AI = 2


def get_move(board, ai_hand):

    best_score = -9999

    best_move = None

    # Check every legal move
    for row in range(10):

        for col in range(10):

            board_card = board[row][col]["card"]

            board_chip = board[row][col]["chip"]

            # Legal move
            if board_card in ai_hand and board_chip == 0:

                # Simulate move
                board[row][col]["chip"] = AI

                score = evaluate_board(board)

                # Undo move
                board[row][col]["chip"] = 0

                # Best move
                if score > best_score:

                    best_score = score

                    best_move = (
                        row,
                        col,
                        board_card
                    )

    return best_move