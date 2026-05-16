import pygame

menu_background = pygame.image.load(
    "assets/menu_bg.jpg"
)

menu_background = pygame.transform.scale(
    menu_background,
    (800, 720)
)

# =====================================
# BUTTONS
# =====================================

easy_button = pygame.Rect(250, 190, 300, 80)

medium_button = pygame.Rect(250, 310, 300, 80)

hard_button = pygame.Rect(250, 430, 300, 80)


# =====================================
# DRAW MENU
# =====================================

def draw_menu(screen):

    # Background image
    screen.blit(menu_background, (0, 0))

    # Dark overlay for readability
    overlay = pygame.Surface((800, 720))

    overlay.set_alpha(110)

    overlay.fill((0, 0, 0))

    screen.blit(overlay, (0, 0))

    # Fonts
    title_font = pygame.font.SysFont(
        "Arial",
        70,
        bold=True
    )

    button_font = pygame.font.SysFont(
        "Arial",
        40,
        bold=True
    )

    subtitle_font = pygame.font.SysFont(
        "Arial",
        24,
        bold=True
    )

    # =====================================
    # TITLE CARD
    # =====================================

    title_rect = pygame.Rect(
        140,
        40,
        520,
        100
    )

    # Shadow
    shadow_rect = pygame.Rect(
        145,
        45,
        520,
        100
    )

    pygame.draw.rect(
        screen,
        (30, 30, 30),
        shadow_rect,
        border_radius=25
    )

    # Main card
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        title_rect,
        border_radius=25
    )

    # Gold border
    pygame.draw.rect(
        screen,
        (255, 215, 0),
        title_rect,
        5,
        border_radius=25
    )

    # Title text
    title = title_font.render(
        "SEQUENCE AI",
        True,
        (20, 20, 20)
    )

    title_text_rect = title.get_rect(
        center=title_rect.center
    )

    screen.blit(title, title_text_rect)

    # =====================================
    # SUBTITLE CARD
    # =====================================

    subtitle_rect = pygame.Rect(
        220,
        150,
        360,
        50
    )

    subtitle_shadow = pygame.Rect(
        224,
        154,
        360,
        50
    )

    pygame.draw.rect(
        screen,
        (40, 40, 40),
        subtitle_shadow,
        border_radius=15
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        subtitle_rect,
        border_radius=15
    )

    pygame.draw.rect(
        screen,
        (0, 0, 0),
        subtitle_rect,
        2,
        border_radius=15
    )

    subtitle = subtitle_font.render(
        "Choose Difficulty Level",
        True,
        (20, 20, 20)
    )

    subtitle_text_rect = subtitle.get_rect(
        center=subtitle_rect.center
    )

    screen.blit(subtitle, subtitle_text_rect)

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
# DRAW BUTTON
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
        (30, 30, 30),
        shadow_rect,
        border_radius=20
    )

    # Main button
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

    # Text
    text_surface = font.render(
        text,
        True,
        (255, 255, 255)
    )

    text_rect = text_surface.get_rect(
        center=rect.center
    )

    screen.blit(text_surface, text_rect)


# =====================================
# HANDLE BUTTON CLICKS
# =====================================

def handle_menu_click(pos):

    if easy_button.collidepoint(pos):
        return "easy"

    elif medium_button.collidepoint(pos):
        return "medium"

    elif hard_button.collidepoint(pos):
        return "hard"

    return None