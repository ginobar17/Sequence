from ai.evaluation import evaluate_board

PLAYER = 1
AI = 2


def get_move(board, ai_hand):

    best_score = -9999

    best_move = None

    # =====================================
    # TRY EVERY AI MOVE
    # =====================================

    for row in range(10):

        for col in range(10):

            board_card = board[row][col]["card"]

            board_chip = board[row][col]["chip"]

            # Legal move
            if board_card in ai_hand and board_chip == 0:

                # Simulate AI move
                board[row][col]["chip"] = AI

                # Simulate player response
                opponent_score = simulate_player_response(board)

                # Final score
                final_score = evaluate_board(board) - opponent_score

                # Undo move
                board[row][col]["chip"] = 0

                # Store best move
                if final_score > best_score:

                    best_score = final_score

                    best_move = (
                        row,
                        col,
                        board_card
                    )

    return best_move


# =====================================
# SIMULATE PLAYER RESPONSE
# =====================================

def simulate_player_response(board):

    worst_case = -9999

    # Pretend player can move anywhere useful
    for row in range(10):

        for col in range(10):

            if board[row][col]["chip"] == 0:

                # Simulate player move
                board[row][col]["chip"] = PLAYER

                score = evaluate_board(board)

                # Undo move
                board[row][col]["chip"] = 0

                # Strongest player response
                if score > worst_case:
                    worst_case = score

    return worst_case