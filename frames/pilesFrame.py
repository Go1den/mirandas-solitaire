from tkinter import Frame, Label, GROOVE, CENTER, messagebox

from PIL import ImageTk, Image

from windows.endOfDrawPileWindow import EndOfDrawPileWindow

class PilesFrame:
    def __init__(self, parent):
        self.frame = Frame(parent.window, relief=GROOVE, bd=2)
        self.parent = parent

        self.cardBackImage = ImageTk.PhotoImage(Image.open("cards/red_back.png"))
        self.blankImage = ImageTk.PhotoImage(Image.open("cards/blank.png"))

        self.labels = []
        self.labelDrawPile = None

        self.initializeFrame()

    def initializeFrame(self):
        for x in range(1, 8):
            label = Label(self.frame, image=self.parent.playArea.piles[x][-1].image)
            label.bind("<Button-1>", self.onPileClick)
            label.grid(row=0, column=x - 1, padx=8, pady=8)
            self.labels.append(label)
        for x in range(8, 11):
            label = Label(self.frame, image=self.parent.playArea.piles[x][-1].image)
            label.bind("<Button-1>", self.onPileClick)
            label.grid(row=1, column=x - 8, padx=8, pady=8)
            self.labels.append(label)
        self.labelDrawPile = Label(self.frame, image=self.cardBackImage)
        self.labelDrawPile.bind("<Button-1>", self.onDrawPileClick)
        self.labelDrawPile.grid(row=1, column=3, padx=8, pady=8)
        for x in range(11, 14):
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

    def onDrawPileClick(self, e):
        if len(self.parent.playArea.drawPile) > 0:
            self.parent.currentPileFrame.clear()
            self.parent.pilesFrame.updateAllImages()
            cards = self.parent.playArea.draw()
            if len(cards) > 0:
                self.parent.playArea.currentPile = cards[0].rank
                self.labels[cards[0].rank - 1].configure(image=self.blankImage)
                self.parent.currentPileFrame.selectNewPile(cards)
            if len(self.parent.playArea.drawPile) == 0:
                self.labelDrawPile.configure(image=self.blankImage, text="Close\nLast\nPile", compound=CENTER)
        elif self.labelDrawPile.cget("text") == "Close\nLast\nPile":
            self.parent.currentPileFrame.clear()
            self.parent.pilesFrame.updateAllImages()
            self.parent.playArea.currentPile = 0
            self.parent.currentPileFrame.selectNewPile([])
            self.labelDrawPile.configure(image=self.blankImage, text="", compound=None)
            if self.isGameInFinalPhase():
                EndOfDrawPileWindow(self.parent)
                # messagebox.showinfo("Draw Pile Exhausted", "You have run out of cards in the draw pile. You may now move cards between ascending and descending piles.")

    def updateAllImages(self):
        index = 0
        for label in self.labels:
            index += 1
            if len(self.parent.playArea.piles[index]) > 0:
                label.configure(image=self.parent.playArea.piles[index][-1].image)
            else:
                label.configure(image=self.blankImage)

    def updatePileImage(self, pile):
        if self.parent.playArea.currentPile != pile and len(self.parent.playArea.piles[pile]) > 0:
            self.labels[pile-1].configure(image=self.parent.playArea.piles[pile][-1].image)
        else:
            self.labels[pile-1].configure(image=self.blankImage)

    def isGameInFinalPhase(self):
        return len(self.parent.playArea.drawPile) == 0 and self.labelDrawPile.cget("text") == ""
