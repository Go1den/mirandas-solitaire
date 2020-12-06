from tkinter import Frame, Label

from PIL import ImageTk, Image

class PilesFrame:
    def __init__(self, parent):
        self.frame = Frame(parent.window)
        self.parent = parent

        self.cardBackImage = ImageTk.PhotoImage(Image.open("cards/red_back.png"))
        self.blankImage = ImageTk.PhotoImage(Image.open("cards/blank.png"))

        self.labels = []
        self.labelDrawPile = None

        self.initializeFrame()

    def initializeFrame(self):
        pile = 0
        for x in range(1, 8):
            pile += 1
            label = Label(self.frame, image=self.parent.playArea.piles[x][-1].image)
            label.bind("<Button-1>", self.onPileClick)
            label.grid(row=0, column=x - 1, padx=8, pady=8)
            self.labels.append(label)
        for x in range(8, 11):
            pile += 1
            label = Label(self.frame, image=self.parent.playArea.piles[x][-1].image)
            label.bind("<Button-1>", self.onPileClick)
            label.grid(row=1, column=x - 8, padx=8, pady=8)
            self.labels.append(label)
        self.labelDrawPile = Label(self.frame, image=self.cardBackImage)
        self.labelDrawPile.grid(row=1, column=3, padx=8, pady=8)
        for x in range(11, 14):
            pile += 1
            label = Label(self.frame, image=self.parent.playArea.piles[x][-1].image)
            label.bind("<Button-1>", self.onPileClick)
            label.grid(row=1, column=x - 7, padx=8, pady=8)
            self.labels.append(label)

    def onPileClick(self, e):
        pile = self.labels.index(e.widget) + 1
        if 0 < pile < 14:
            self.parent.playArea.playCardFromPile(pile)
            self.updatePileImage(pile)
            self.parent.playedFrameAsc.updateAllImages()
            self.parent.playedFrameDesc.updateAllImages()

    def updateAllImages(self):
        index = 0
        for label in self.labels:
            index += 1
            label.configure(image=self.parent.playArea.piles[index][-1].image)

    def updatePileImage(self, pile):
        self.labels[pile-1].configure(image=self.parent.playArea.piles[pile][-1].image)
