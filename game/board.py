import random

ROWS = 10
COLS = 10

EMPTY = 0
PLAYER = 1
AI = 2

# =====================================
# CARD LIST
# =====================================

cards = [
    "AH", "2H", "3H", "4H", "5H",
    "6H", "7H", "8H", "9H", "10H",

    "AS", "2S", "3S", "4S", "5S",
    "6S", "7S", "8S", "9S", "10S",

    "AC", "2C", "3C", "4C", "5C",
    "6C", "7C", "8C", "9C", "10C",

    "AD", "2D", "3D", "4D", "5D",
    "6D", "7D", "8D", "9D", "10D"
    
    "J1", "J2", "J3", "J4"
]

# =====================================
# CREATE BOARD
# =====================================

def create_board():

    shuffled = cards * 3

    random.shuffle(shuffled)

    board = []

    index = 0

    for row in range(ROWS):

        current_row = []

        for col in range(COLS):

            current_row.append({
                "card": shuffled[index],
                "chip": EMPTY
            })

            index += 1

        board.append(current_row)

    return board


# =====================================
# CREATE DECK
# =====================================

def create_deck():

    deck = cards * 2

    random.shuffle(deck)

    return deck


# =====================================
# DRAW CARDS
# =====================================

def draw_cards(deck, amount):

    hand = []

    for _ in range(amount):

        if deck:
            hand.append(deck.pop())

    return hand