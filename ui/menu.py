import pygame

easy_button = pygame.Rect(250, 180, 300, 60)
medium_button = pygame.Rect(250, 300, 300, 60)
hard_button = pygame.Rect(250, 420, 300, 60)


def draw_menu(screen):
    font = pygame.font.SysFont(None, 50)
    screen.fill((240, 240, 240))

    title = font.render("Sequence AI", True, (0, 0, 0))
    screen.blit(title, (280, 80))

    pygame.draw.rect(screen, (0, 200, 0), easy_button)
    pygame.draw.rect(screen, (255, 200, 0), medium_button)
    pygame.draw.rect(screen, (200, 0, 0), hard_button)

    easy_text = font.render("Easy", True, (255, 255, 255))
    medium_text = font.render("Medium", True, (255, 255, 255))
    hard_text = font.render("Hard", True, (255, 255, 255))

    screen.blit(easy_text, (350, 195))
    screen.blit(medium_text, (330, 315))
    screen.blit(hard_text, (350, 435))


def handle_menu_click(pos):

    if easy_button.collidepoint(pos):
        return "easy"

    elif medium_button.collidepoint(pos):
        return "medium"

    elif hard_button.collidepoint(pos):
        return "hard"

    return None