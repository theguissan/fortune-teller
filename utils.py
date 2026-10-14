import random
from deck import Deck
from arcana import Arcana


X_SIZE = 30
Y_SIZE = 20


def shuffle_deck(deck: Deck) -> Deck:
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]
    return deck


def one_card_game(deck: Deck):
    shuffled_deck = shuffle_deck(deck)

    print_card(shuffled_deck[0])


def three_card_game(deck: Deck):
    shuffled_deck = shuffle_deck(deck)

    for i in range(3):
        print_card(shuffled_deck[i])


def aphrodite_temple(deck: Deck):
    shuffled_deck = shuffle_deck(deck)

    for i in range(7):
        print_card(shuffled_deck[i])


def print_card(card: Arcana):
    aux = 0
    string_size = len(card.name)

    x_border = ""
    y_border = ""

    # position cal to center the arcana name
    card_position = int((X_SIZE - string_size) / 2) - 1

    for _ in range(X_SIZE):
        x_border += "-"

    for y in range(Y_SIZE):
        y_border += "|"
        for x in range(X_SIZE - 1):
            if x < X_SIZE - 2:
                if y == Y_SIZE / 2 and (
                    x >= card_position and x < card_position + string_size
                ):
                    y_border += f"{card.name[aux]}"
                    aux += 1
                else:
                    y_border += " "
            else:
                y_border += "|"

        if y < Y_SIZE - 1:
            y_border += "\n"

    print(x_border)
    print(y_border)
    print(x_border)
