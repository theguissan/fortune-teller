from arcana import Arcana

type Deck = list[Arcana]

major_names = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",
]


suits = ["Wands", "Cups", "Swords", "Pentacles"]
ranks = [
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Page",
    "Knight",
    "Queen",
    "King",
]

major_arcanas: Deck = [Arcana(name) for name in major_names]
minor_arcanas: Deck = [Arcana(f"{rank} of {suit}") for suit in suits for rank in ranks]
full_deck: Deck = major_arcanas + minor_arcanas
