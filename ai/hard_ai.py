from ai.evaluation import evaluate_board

PLAYER = 1
AI = 2

MAX_DEPTH = 2


# GET ALL LEGAL MOVES

def get_legal_moves(board, hand):

        moves = []

        for row in range(10):

            for col in range(10):

                board_card = board[row][col]["card"]

                board_chip = board[row][col]["chip"]

                # Skip occupied
                if board_chip != 0:
                    continue

                # =====================================
                # CHECK NEARBY ACTIVITY
                # =====================================

                nearby = False

                for r in range(max(0, row - 1), min(10, row + 2)):

                    for c in range(max(0, col - 1), min(10, col + 2)):

                        if board[r][c]["chip"] != 0:
                            nearby = True

                # Ignore isolated positions
                if not nearby:
                    continue

                # =====================================
                # NORMAL CARD MATCH
                # =====================================

                if board_card in hand:

                    moves.append((row, col, board_card))

                # =====================================
                # JOKER SUPPORT
                # =====================================

                elif any(card.startswith("J") for card in hand):

                    joker = next(
                        card for card in hand
                        if card.startswith("J")
                    )

                    moves.append((row, col, joker))

        # =====================================
        # FALLBACK FOR EARLY GAME
        # =====================================

        if not moves:

            for row in range(10):

                for col in range(10):

                    board_card = board[row][col]["card"]

                    board_chip = board[row][col]["chip"]

                    if board_chip != 0:
                        continue

                    if board_card in hand:
                        moves.append((row, col, board_card))

        return moves


# MAIN AI MOVE

def get_move(board, ai_hand):

    best_score = -99999

    best_move = None

    alpha = -99999
    beta = 99999

    legal_moves = get_legal_moves(board, ai_hand)

    for move in legal_moves:

        row, col, used_card = move

        # Simulate AI move
        board[row][col]["chip"] = AI

        # Remove used card temporarily
        temp_hand = ai_hand.copy()
        temp_hand.remove(used_card)

        score = minimax(
            board,
            MAX_DEPTH,
            False,
            alpha,
            beta,
            temp_hand
        )

        # Undo move
        board[row][col]["chip"] = 0

        if score > best_score:

            best_score = score

            best_move = move

        alpha = max(alpha, best_score)

    return best_move


# MINIMAX WITH ALPHA-BETA PRUNING

def minimax(
        board,
        depth,
        maximizing_player,
        alpha,
        beta,
        ai_hand
):

    # STOP CONDITION

    if depth == 0:
        return evaluate_board(board)

    # MAXIMIZING PLAYER (AI)

    if maximizing_player:

        max_eval = -99999

        legal_moves = get_legal_moves(board, ai_hand)

        if not legal_moves:
            return evaluate_board(board)

        for move in legal_moves:

            row, col, used_card = move

            # Simulate move
            board[row][col]["chip"] = AI

            # Temporary hand update
            temp_hand = ai_hand.copy()

            if used_card in temp_hand:
                temp_hand.remove(used_card)

            eval_score = minimax(
                board,
                depth - 1,
                False,
                alpha,
                beta,
                temp_hand
            )

            # Undo move
            board[row][col]["chip"] = 0

            max_eval = max(max_eval, eval_score)

            alpha = max(alpha, eval_score)

            # ALPHA-BETA PRUNING

            if beta <= alpha:
                break

        return max_eval

    # MINIMIZING PLAYER

    else:

        min_eval = 99999

        # Simulate possible player moves
        for row in range(10):

            for col in range(10):

                if board[row][col]["chip"] == 0:

                    # Simulate player move
                    board[row][col]["chip"] = PLAYER

                    eval_score = minimax(
                        board,
                        depth - 1,
                        True,
                        alpha,
                        beta,
                        ai_hand
                    )

                    # Undo move
                    board[row][col]["chip"] = 0

                    min_eval = min(min_eval, eval_score)

                    beta = min(beta, eval_score)

                    # =====================================
                    # ALPHA-BETA PRUNING
                    # =====================================

                    if beta <= alpha:
                        break

        return min_eval
