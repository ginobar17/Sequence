import pygame
import sys
from game.board import create_board
from ui.renderer import draw_board
from ai.easy_ai import get_move
from game.rules import check_winner

from ui.menu import draw_menu, handle_menu_click

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sequence AI")

icon = pygame.image.load("sequence.png")
pygame.display.set_icon(icon)

# States
MENU = 0
GAME = 1

current_state = MENU

difficulty = None

board =create_board()
PLAYER = 1
AI = 2

current_turn = PLAYER
game_over = False
winner = None

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if current_state == MENU:

                selected = handle_menu_click(event.pos)

                if selected:
                    difficulty = selected
                    current_state = GAME

            elif current_state == GAME:

                mouse_x, mouse_y = event.pos

                row = mouse_y // 60
                col = mouse_x // 60
                if board[row][col] == 0 and current_turn == PLAYER:

                    board[row][col] = PLAYER
                    if check_winner(board, PLAYER):

                        winner = "PLAYER"

                        game_over = True

                    if not game_over:

                        current_turn = AI
                        ai_move = get_move(board)

                        if ai_move:

                            ai_row, ai_col = ai_move

                            board[ai_row][ai_col] = AI

                            if check_winner(board, AI):

                                winner = "AI"

                                game_over = True

                    if not game_over:
                        current_turn = PLAYER

    # DRAWING
    if current_state == MENU:
        draw_menu(screen)

    elif current_state == GAME:

        draw_board(screen, board)

    pygame.display.update()

pygame.quit()
sys.exit()