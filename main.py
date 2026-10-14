from deck import full_deck
from utils import one_card_game, three_card_game, aphrodite_temple


def main():
    deck = full_deck

    print("\n Hi baby, wanna a fortune telling?")

    print("\nType the desired read")
    print("1) One card read")
    print("2) Three card read")
    print("3) Aphrodite Temple")

    match input("Option: "):
        case "1":
            one_card_game(deck)
        case "2":
            three_card_game(deck)
        case "3":
            aphrodite_temple(deck)
        case _:
            print("Ohh you silly, i can't read it")


if __name__ == "__main__":
    main()
