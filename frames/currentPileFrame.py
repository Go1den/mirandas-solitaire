from tkinter import Frame, Label, GROOVE

class CurrentPileFrame:
    def __init__(self, parent):
        self.frame = Frame(parent.window, relief=GROOVE, bd=2, width=640, height=140)
        self.parent = parent

        labelCurrentPile = Label(self.frame, text="Current Pile")
        labelCurrentPile.place(relx=0.9, rely=0.01)

        self.labels = []

    def selectNewPile(self, cards):
        labelCurrentPile = Label(self.frame, text="Current Pile")
        labelCurrentPile.place(relx=0.9, rely=0.01)
        for card in cards:
            label = Label(self.frame, image=card.image)
            label.bind("<Button-1>", self.playCard)
            label.place(x=4+(40*(cards.index(card))), y=4)
            self.labels.append(label)
        if self.parent.playArea.currentPile > 0:
            self.parent.pilesFrame.labels[self.parent.playArea.currentPile - 1].configure(text=str(len(cards)))

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.labels = []

    def playCard(self, e):
        index = self.labels.index(e.widget)
        if self.parent.playArea.playCardFromCurrentPile(index):
            self.parent.currentPileFrame.clear()
            cards = self.parent.playArea.piles[self.parent.playArea.currentPile]
            self.selectNewPile(cards)
            self.parent.playedFrameAsc.updateAllImages()
            self.parent.playedFrameDesc.updateAllImages()
            self.parent.pilesFrame.labels[self.parent.playArea.currentPile-1].configure(text=str(len(cards)))


