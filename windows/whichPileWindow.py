from tkinter import Frame, Label, Toplevel

from card import Card
from windows.windowHelper import WindowHelper

class WhichPileWindow:
    def __init__(self, card1: Card, card2: Card, parent):
        self.window = Toplevel(parent.window)
        self.window.withdraw()
        self.card1 = card1
        self.card2 = card2
        self.parent = parent

        self.gridFrames()
        self.labelAsc = Label(self.frame, image=self.card1.image)
        self.labelDesc = Label(self.frame, image=self.card2.image)

        self.labels = [self.labelAsc, self.labelDesc]

        self.frame = Frame(self.window)

        WindowHelper.initializeWindow(self.window, self.parent, 300, 200, 100, 100, "Select pile to play on.")
        self.addCards()
        WindowHelper.finalizeWindow(self.window, self.parent)

    def gridFrames(self):
        self.frame.grid(row=0, padx=4, pady=4)

    def addCards(self):
        labelWhich = Label(self.frame, text="Which pile do you want to play on?")
        labelWhich.grid(row=0, column=0, columnspan=2, padx=4, pady=4)
        self.labelAsc.bind("<Button-1>", self.selectPile)
        self.labelAsc.grid(row=1, column=0, padx=4, pady=4)
        self.labelDesc.bind("<Button-1>", self.selectPile)
        self.labelDesc.grid(row=1, column=1, padx=4, pady=4)

    def selectPile(self, e):
        self.parent.playArea.selectedPile = self.labels.index(e) + 1
        self.window.destroy()
