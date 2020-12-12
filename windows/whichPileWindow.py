from tkinter import Frame, Label, Toplevel, TOP

from card import Card
from windows.windowHelper import WindowHelper

class WhichPileWindow:
    def __init__(self, card1: Card, card2: Card, parent):
        self.window = Toplevel(parent.window)
        self.window.withdraw()
        self.card1 = card1
        self.card2 = card2
        self.parent = parent

        self.frame = Frame(self.window)
        self.gridFrames()
        self.labelAsc = Label(self.frame, image=self.card1.image, text="Ascending", compound=TOP)
        self.labelDesc = Label(self.frame, image=self.card2.image, text="Descending", compound=TOP)
        self.labels = None

        WindowHelper.initializeWindow(self.window, self.parent, 196, 160, 322, 270, "Select pile to play on.")
        self.addCards()
        WindowHelper.finalizeWindow(self.window, self.parent)

    def gridFrames(self):
        self.frame.grid(row=0, padx=4, pady=4)

    def addCards(self):
        self.labelAsc.bind("<Button-1>", self.selectPile)
        self.labelAsc.grid(row=0, column=0, padx=4, pady=4)
        self.labelDesc.bind("<Button-1>", self.selectPile)
        self.labelDesc.grid(row=0, column=1, padx=4, pady=4)
        self.labels = [self.labelAsc, self.labelDesc]

    def selectPile(self, e):
        self.parent.playArea.selectedPile = self.labels.index(e.widget) + 1
        self.window.destroy()
