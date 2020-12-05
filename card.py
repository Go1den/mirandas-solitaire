from PIL import Image, ImageTk

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.filePath = "images/" + str(rank) + str(suit) + ".png"
        self.image = ImageTk.PhotoImage(Image.open(self.filePath))
