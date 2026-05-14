import pygame

CELL_SIZE = 60

ROWS = 10
COLS = 10


# GET CARD COLOR

def get_card_color(card):

    if "H" in card or "D" in card:
        return (200, 0, 0)

    return (0, 0, 0)

# DRAW BOARD

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

    # Background
    screen.fill((30, 120, 70))

    font = pygame.font.SysFont("Arial", 18, bold=True)

    hand_font = pygame.font.SysFont("Arial", 28, bold=True)

    # DRAW BOARD

    for row in range(ROWS):

        for col in range(COLS):

            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            # HIGHLIGHT VALID MOVES

            highlight = (
                selected_card_value is not None and
                board[row][col]["chip"] == 0 and
                (
                    board[row][col]["card"] == selected_card_value
                    or
                    selected_card_value.startswith("J")
                )
            )

            # Shadow
            shadow_rect = pygame.Rect(
                rect.x + 2,
                rect.y + 2,
                rect.width,
                rect.height
            )

            pygame.draw.rect(
                screen,
                (40, 40, 40),
                shadow_rect,
                border_radius=8
            )

            # Highlighted card
            if highlight:

                pygame.draw.rect(
                    screen,
                    (255, 255, 120),
                    rect,
                    border_radius=8
                )

            else:

                pygame.draw.rect(
                    screen,
                    (255, 255, 255),
                    rect,
                    border_radius=8
                )

            # Border
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                rect,
                2,
                border_radius=8
            )

            # CARD TEXT

            card = board[row][col]["card"]

            color = get_card_color(card)

            text = font.render(card, True, color)

            screen.blit(text, (rect.x + 8, rect.y + 6))

            # Small bottom-right corner card
            small_text = font.render(card, True, color)

            screen.blit(
                small_text,
                (rect.x + 28, rect.y + 35)
            )

            # PLAYER CHIP

            if board[row][col]["chip"] == 1:

                pygame.draw.circle(
                    screen,
                    (0, 180, 255),
                    rect.center,
                    15
                )

                pygame.draw.circle(
                    screen,
                    (255, 255, 255),
                    rect.center,
                    15,
                    2
                )

            # AI CHIP

            elif board[row][col]["chip"] == 2:

                pygame.draw.circle(
                    screen,
                    (255, 70, 70),
                    rect.center,
                    15
                )

                pygame.draw.circle(
                    screen,
                    (255, 255, 255),
                    rect.center,
                    15,
                    2
                )

    # PLAYER HAND

    for index, card in enumerate(player_hand):

        x_pos = 20 + (index * 120)

        y_pos = 620

        card_rect = pygame.Rect(x_pos, y_pos, 100, 55)

        # Shadow
        shadow_rect = pygame.Rect(
            x_pos + 3,
            y_pos + 3,
            100,
            55
        )

        pygame.draw.rect(
            screen,
            (40, 40, 40),
            shadow_rect,
            border_radius=10
        )

        # Selected card
        if selected_card == index:

            pygame.draw.rect(
                screen,
                (255, 255, 120),
                card_rect,
                border_radius=10
            )

        else:

            pygame.draw.rect(
                screen,
                (255, 255, 255),
                card_rect,
                border_radius=10
            )

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            card_rect,
            2,
            border_radius=10
        )

        color = get_card_color(card)

        text = hand_font.render(card, True, color)

        text_rect = text.get_rect(center=card_rect.center)

        screen.blit(text, text_rect)

    # TURN DISPLAY

    if current_turn == 1:

        turn_text = hand_font.render(
            "PLAYER TURN",
            True,
            (255, 255, 255)
        )

    else:

        turn_text = hand_font.render(
            "AI TURN",
            True,
            (255, 255, 255)
        )

    screen.blit(turn_text, (620, 620))

    # DIFFICULTY

    diff_text = font.render(
        f"Difficulty: {difficulty.upper()}",
        True,
        (255, 255, 255)
    )

    screen.blit(diff_text, (620, 660))

    # WINNER

    if winner:

        win_font = pygame.font.SysFont("Arial", 40, bold=True)

        win_text = win_font.render(
            f"{winner} WINS!",
            True,
            (255, 255, 0)
        )

        screen.blit(win_text, (260, 300))
