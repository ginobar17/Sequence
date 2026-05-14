import pygame

# =====================================
# BUTTONS
# =====================================

easy_button = pygame.Rect(250, 180, 300, 80)

medium_button = pygame.Rect(250, 300, 300, 80)

hard_button = pygame.Rect(250, 420, 300, 80)


# =====================================
# DRAW MENU
# =====================================

def draw_menu(screen):

    # Background
    screen.fill((235, 235, 235))

    # Fonts
    title_font = pygame.font.SysFont("Arial", 70, bold=True)

    button_font = pygame.font.SysFont("Arial", 40, bold=True)

    subtitle_font = pygame.font.SysFont("Arial", 24)

    # =====================================
    # TITLE
    # =====================================

    title = title_font.render(
        "SEQUENCE AI",
        True,
        (30, 30, 30)
    )

    screen.blit(title, (180, 60))

    subtitle = subtitle_font.render(
        "Choose Difficulty Level",
        True,
        (80, 80, 80)
    )

    screen.blit(subtitle, (280, 130))

    # =====================================
    # DRAW BUTTONS
    # =====================================

    draw_button(
        screen,
        easy_button,
        (40, 170, 90),
        "Easy",
        button_font
    )

    draw_button(
        screen,
        medium_button,
        (230, 180, 40),
        "Medium",
        button_font
    )

    draw_button(
        screen,
        hard_button,
        (200, 60, 60),
        "Hard",
        button_font
    )


# =====================================
# DRAW SINGLE BUTTON
# =====================================

def draw_button(screen, rect, color, text, font):

    # Shadow
    shadow_rect = pygame.Rect(
        rect.x + 5,
        rect.y + 5,
        rect.width,
        rect.height
    )

    pygame.draw.rect(
        screen,
        (170, 170, 170),
        shadow_rect,
        border_radius=20
    )

    # Main rounded button
    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=20
    )

    # White border
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        rect,
        3,
        border_radius=20
    )

    # Button text
    text_surface = font.render(
        text,
        True,
        (255, 255, 255)
    )

    text_rect = text_surface.get_rect(center=rect.center)

    screen.blit(text_surface, text_rect)


# =====================================
# HANDLE CLICKS
# =====================================

def handle_menu_click(pos):

    if easy_button.collidepoint(pos):
        return "easy"

    elif medium_button.collidepoint(pos):
        return "medium"

    elif hard_button.collidepoint(pos):
        return "hard"

    return None