from tkinter import Frame, Label, Toplevel, Button, E, LEFT

from windows.windowHelper import WindowHelper

class HowToPlayWindow:
    def __init__(self, parent):
        self.window = Toplevel(parent.window)
        self.window.withdraw()
        self.parent = parent

        self.frame = Frame(self.window)
        self.gridFrames()

        WindowHelper.initializeWindow(self.window, self.parent, 360, 142, 240, 290, "How To Play")
        self.populateFrame()
        WindowHelper.finalizeWindow(self.window, self.parent)

    def gridFrames(self):
        self.frame.grid(row=0, padx=4, pady=4)

    def populateFrame(self):
        label = Label(self.frame, justify=LEFT, text="Try to get all of the cards from Ace to King in the Ascending piles\nand all of the cards from King to Ace in the Descending piles.\nWhen you draw a card, you gain access to all the cards in the\ncorresponding pile. When the draw pile runs out, you can click\nClose Draw Pile to move to the end game where you can also\nmove cards on the top row.")
        label.grid(row=0, padx=4, pady=4)
        okButton = Button(self.frame, text="OK", command=self.close, width=8)
        okButton.grid(row=1, padx=4, pady=4, sticky=E)

    def close(self):
        self.window.destroy()
