from PIL import Image, ImageTk

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.filePath = "cards/" + str(rank) + str(suit) + ".png"
        self.image = ImageTk.PhotoImage(Image.open(self.filePath))

    def getSeedValue(self):
        suits = ["H", "D", "C", "S"]
        seedValue = self.rank + (13 * suits.index(self.suit))
        if seedValue < 27:
            return chr(seedValue + 64)
        else:
            return chr(seedValue + 70)

    def toString(self):
        return str(self.rank) + str(self.suit)
