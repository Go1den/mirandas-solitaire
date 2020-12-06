import random
from typing import List

from card import Card

class Deck:
    def __init__(self):
        self.cards = self.createCards()

    def createCards(self) -> List[Card]:
        cards = []
        for rank in range(1, 14):
            for suit in ["H", "D", "C", "S"]:
                cards.append(Card(rank, suit))
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def getSeed(self) -> str:
        result = ""
        for card in self.cards:
            result += card.getSeedValue()
        return result

    def loadSeed(self, seed):
        cards = []
        for char in seed:
            asciiValue = ord(char)
            if asciiValue < 91:
                asciiValue -= 64
            else:
                asciiValue -= 70
            if asciiValue < 14:
                suit = "H"
            elif asciiValue < 27:
                suit = "D"
            elif asciiValue < 40:
                suit = "C"
            else:
                suit = "S"
            rank = asciiValue % 13
            if rank == 0:
                rank = 13
            cards.append(Card(rank, suit))
        self.cards = cards


