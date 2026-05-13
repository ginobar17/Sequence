import pygame

CELL_SIZE = 60

ROWS = 10
COLS = 10


def draw_board(
        screen,
        board,
        current_turn,
        difficulty,
        player_hand,
        selected_card,
        selected_card_value,
        winner=None
):

    screen.fill((255, 255, 255))

    font = pygame.font.SysFont(None, 24)

    # =====================================
    # DRAW BOARD
    # =====================================

    for row in range(ROWS):

        for col in range(COLS):

            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            # Highlight matching card positions
            if (
                    selected_card_value is not None and
                    board[row][col]["chip"] == 0 and
                    (
                            board[row][col]["card"] == selected_card_value
                            or
                            selected_card_value.startswith("J")
                    )
            ):

                pygame.draw.rect(
                    screen,
                    (255, 255, 0),
                    rect
                )

            # Normal cell
            else:

                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    rect
                )

            # Grid border
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            # DRAW CARD TEXT
            card_text = font.render(
                board[row][col]["card"],
                True,
                (0, 0, 0)
            )

            screen.blit(
                card_text,
                (col * CELL_SIZE + 10, row * CELL_SIZE + 5)
            )

            # PLAYER CHIP
            if board[row][col]["chip"] == 1:

                pygame.draw.circle(
                    screen,
                    (0, 200, 0),
                    rect.center,
                    18
                )

            # AI CHIP
            elif board[row][col]["chip"] == 2:

                pygame.draw.circle(
                    screen,
                    (200, 0, 0),
                    rect.center,
                    18
                )

    # =====================================
    # PLAYER HAND
    # =====================================

    hand_font = pygame.font.SysFont(None, 30)

    y_pos = 620

    for index, card in enumerate(player_hand):

        x_pos = 20 + (index * 120)

        card_rect = pygame.Rect(x_pos, y_pos, 100, 40)

        # Highlight selected card
        if selected_card == index:
            pygame.draw.rect(screen, (0, 200, 0), card_rect)

        else:
            pygame.draw.rect(screen, (180, 180, 180), card_rect)

        text = hand_font.render(card, True, (0, 0, 0))

        screen.blit(text, (x_pos + 25, y_pos + 8))

    # =====================================
    # TURN DISPLAY
    # =====================================

    if current_turn == 1:

        turn_text = hand_font.render(
            "PLAYER TURN",
            True,
            (0, 150, 0)
        )

    else:

        turn_text = hand_font.render(
            "AI TURN",
            True,
            (200, 0, 0)
        )

    screen.blit(turn_text, (620, 620))

    # =====================================
    # WINNER
    # =====================================

    if winner:

        win_text = hand_font.render(
            f"{winner} WINS!",
            True,
            (0, 0, 0)
        )

        screen.blit(win_text, (620, 660))