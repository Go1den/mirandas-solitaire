from tkinter import Frame, Label, GROOVE

class CurrentPileFrame:
    def __init__(self, parent):
        self.frame = Frame(parent.window, relief=GROOVE, bd=2)
        self.parent = parent

        self.labels = []

    def selectNewPile(self, cards):
        for card in cards:
            label = Label(self.frame, image=card.image)
            label.bind("<Button-1>", self.playCard)
            label.grid(row=0, column=cards.index(card), padx=4, pady=4)
            self.labels.append(label)

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


