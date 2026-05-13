import pygame

CELL_SIZE = 60
ROWS = 10
COLS = 10


def draw_board(screen, board, winner=None):

    screen.fill((255, 255, 255))

    for row in range(ROWS):

        for col in range(COLS):

            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            # Draw player chip
            if board[row][col] == 1:

                pygame.draw.circle(
                    screen,
                    (0, 200, 0),
                    rect.center,
                    20
                )

            # Draw AI chip
            elif board[row][col] == 2:

                pygame.draw.circle(
                    screen,
                    (200, 0, 0),
                    rect.center,
                    20
                )