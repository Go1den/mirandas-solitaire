from copy import copy

from card import Card
from deck import Deck

class PlayArea:
    def __init__(self):
        self.piles = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: [],
            13: []
        }
        self.drawPile = []
        self.scorePiles = {
            "ascH": [Card(0, "H")],
            "ascD": [Card(0, "D")],
            "ascC": [Card(0, "C")],
            "ascS": [Card(0, "S")],
            "descH": [Card(14, "H")],
            "descD": [Card(14, "D")],
            "descC": [Card(14, "C")],
            "descS": [Card(14, "S")]
        }

    def deal(self, deck: Deck):
        pileIndex = 1
        cardsToDeal = copy(deck.cards)
        while len(cardsToDeal) > 0:
            currentCard = cardsToDeal.pop(0)
            self.piles[pileIndex].append(currentCard)
            if currentCard.rank == pileIndex and len(cardsToDeal) > 0:
                self.drawPile.append(cardsToDeal.pop(0))
            if currentCard.rank == 1 and len(cardsToDeal) > 0:
                self.drawPile.append(cardsToDeal.pop(0))
            if currentCard.rank == 1 and currentCard.rank == pileIndex and len(cardsToDeal) > 0:
                self.drawPile.append(cardsToDeal.pop(0))
                if len(cardsToDeal) > 0:
                    self.drawPile.append(cardsToDeal.pop(0))
            if (currentCard.rank == 10 or currentCard.rank == 13) and len(cardsToDeal) > 0:
                self.drawPile.append(cardsToDeal.pop(0))
            pileIndex = (pileIndex % 13) + 1

    # Used for debugging, remove when releasing
    def printAllPiles(self):
        totalCards = 0
        for x in range(1, 14):
            print("Pile " + str(x))
            for card in self.piles[x]:
                print(card.toString())
                totalCards += 1

        print("Draw pile")
        for card in self.drawPile:
            totalCards += 1
            print(card.toString())

        print("Total cards: " + str(totalCards))

    def playCardFromPile(self, pile):
        if len(self.piles[pile]) > 0:
            card = self.piles[pile][-1]
            ascCard = self.scorePiles["asc" + card.suit][-1]
            if card.rank - 1 == ascCard.rank:
                print("Asc card is playable")
                self.scorePiles["asc" + card.suit].append(self.piles[pile].pop())
                for card in self.scorePiles["asc" + card.suit]:
                    print(card.toString())
            else:
                descCard = self.scorePiles["desc" + card.suit][-1]
                if card.rank + 1 == descCard.rank:
                    print("Desc card is playable")
                    self.scorePiles["desc" + card.suit].append(self.piles[pile].pop())
                    for card in self.scorePiles["desc" + card.suit]:
                        print(card.toString())