from copy import copy
from typing import List

from card import Card
from deck import Deck
from windows.whichPileWindow import WhichPileWindow

class PlayArea:
    def __init__(self, parent):
        self.parent = parent
        self.selectedPile = 0
        self.currentPile = 0
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

    def draw(self) -> List[Card]:
        if len(self.drawPile) > 0:
            card = self.drawPile.pop()
            self.piles[card.rank].insert(0, card)
            return self.piles[card.rank]
        else:
            return []

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

    def playCardFromCurrentPile(self, index) -> bool:
        if len(self.piles[self.currentPile]) > 0:
            card = self.piles[self.currentPile][index]
            ascCard = self.scorePiles["asc" + card.suit][-1]
            descCard = self.scorePiles["desc" + card.suit][-1]
            if card.rank - 1 == ascCard.rank:
                if card.rank + 1 == descCard.rank:
                    self.selectedPile = 0
                    WhichPileWindow(ascCard, descCard, self.parent)
                    if self.selectedPile == 1:
                        self.scorePiles["asc" + card.suit].append(self.piles[self.currentPile].pop(index))
                        return True
                    elif self.selectedPile == 2:
                        self.scorePiles["desc" + card.suit].append(self.piles[self.currentPile].pop(index))
                        return True
                else:
                    self.scorePiles["asc" + card.suit].append(self.piles[self.currentPile].pop(index))
                    return True
            else:
                if card.rank + 1 == descCard.rank:
                    self.scorePiles["desc" + card.suit].append(self.piles[self.currentPile].pop(index))
                    return True
        return False

    def playCardFromPile(self, pile) -> bool:
        if len(self.piles[pile]) > 0:
            card = self.piles[pile][-1]
            ascCard = self.scorePiles["asc" + card.suit][-1]
            descCard = self.scorePiles["desc" + card.suit][-1]
            if card.rank - 1 == ascCard.rank:
                if card.rank + 1 == descCard.rank:
                    self.selectedPile = 0
                    WhichPileWindow(ascCard, descCard, self.parent)
                    if self.selectedPile == 1:
                        self.scorePiles["asc" + card.suit].append(self.piles[pile].pop())
                        return True
                    elif self.selectedPile == 2:
                        self.scorePiles["desc" + card.suit].append(self.piles[pile].pop())
                        return True
                else:
                    self.scorePiles["asc" + card.suit].append(self.piles[pile].pop())
                    return True
            else:
                if card.rank + 1 == descCard.rank:
                    self.scorePiles["desc" + card.suit].append(self.piles[pile].pop())
                    return True
        return False
