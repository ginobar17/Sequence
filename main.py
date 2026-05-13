import pygame
import sys

from game.board import (
    create_board,
    create_deck,
    draw_cards,
    PLAYER,
    AI
)

from game.rules import check_winner

from ui.menu import draw_menu, handle_menu_click
from ui.renderer import draw_board

from ai.easy_ai import get_move as easy_move
from ai.medium_ai import get_move as medium_move
from ai.hard_ai import get_move as hard_move

pygame.init()

WIDTH = 800
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sequence AI")

# =====================================
# GAME STATES
# =====================================

MENU = 0
GAME = 1

current_state = MENU

# =====================================
# GAME VARIABLES
# =====================================

difficulty = None

board = create_board()

deck = create_deck()

player_hand = draw_cards(deck, 5)

ai_hand = draw_cards(deck, 5)

selected_card = None
selected_card_value = None

current_turn = PLAYER

winner = None

game_over = False

running = True

# =====================================
# MAIN LOOP
# =====================================

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # =====================================
        # MENU
        # =====================================

        if event.type == pygame.MOUSEBUTTONDOWN:

            if current_state == MENU:

                selected = handle_menu_click(event.pos)

                if selected:

                    difficulty = selected

                    current_state = GAME

            # =====================================
            # GAME
            # =====================================

            elif current_state == GAME and not game_over:

                mouse_x, mouse_y = event.pos

                # =====================================
                # SELECT CARD
                # =====================================

                if mouse_y >= 620:

                    for index in range(len(player_hand)):

                        x = 20 + (index * 120)

                        rect = pygame.Rect(x, 620, 100, 40)

                        if rect.collidepoint(event.pos):

                            selected_card = index
                            selected_card_value = player_hand[index]

                # =====================================
                # PLACE CHIP
                # =====================================

                else:

                    row = mouse_y // 60
                    col = mouse_x // 60

                    if row >= 10 or col >= 10:
                        continue

                    if selected_card is not None:

                        selected = player_hand[selected_card]

                        board_card = board[row][col]["card"]

                        if (
                                (
                                        selected == board_card
                                        or
                                        selected.startswith("J")
                                )
                                and
                                board[row][col]["chip"] == 0
                        ):

                            board[row][col]["chip"] = PLAYER

                            # Remove used card
                            player_hand.pop(selected_card)

                            # Draw new card
                            if deck:
                                player_hand.append(deck.pop())

                            selected_card = None
                            selected_card_value = None

                            # WIN CHECK
                            if check_winner(board, PLAYER):

                                winner = "PLAYER"

                                game_over = True

                            # =====================================
                            # AI TURN
                            # =====================================

                            if not game_over:

                                current_turn = AI

                                if difficulty == "easy":

                                    ai_move = easy_move(board, ai_hand)

                                elif difficulty == "medium":

                                    ai_move = medium_move(board, ai_hand)

                                else:

                                    ai_move = hard_move(board, ai_hand)

                                if ai_move:

                                    ai_row, ai_col, used_card = ai_move

                                    board[ai_row][ai_col]["chip"] = AI

                                    ai_hand.remove(used_card)

                                    if deck:
                                        ai_hand.append(deck.pop())

                                    if check_winner(board, AI):

                                        winner = "AI"

                                        game_over = True

                                current_turn = PLAYER

    # =====================================
    # DRAWING
    # =====================================

    if current_state == MENU:

        draw_menu(screen)

    elif current_state == GAME:

        draw_board(
            screen,
            board,
            current_turn,
            difficulty,
            player_hand,
            selected_card,
            selected_card_value,
            winner
        )

    pygame.display.update()

pygame.quit()
sys.exit()