from tkinter import Frame, Label

from PIL import ImageTk, Image

class PlayedFrameAsc:
    def __init__(self, parent):
        self.frame = Frame(parent.window)
        self.parent = parent

        self.blankImage = ImageTk.PhotoImage(Image.open("cards/blank.png"))

        self.labelPile1 = None
        self.labelPile2 = None
        self.labelPile3 = None
        self.labelPile4 = None

        self.initializeFrame()

    def initializeFrame(self):
        self.labelPile1 = Label(self.frame, image=self.blankImage)
        self.labelPile1.grid(row=0, column=0, padx=8, pady=8)
        self.labelPile2 = Label(self.frame, image=self.blankImage)
        self.labelPile2.grid(row=0, column=1, padx=8, pady=8)
        self.labelPile3 = Label(self.frame, image=self.blankImage)
        self.labelPile3.grid(row=0, column=2, padx=8, pady=8)
        self.labelPile4 = Label(self.frame, image=self.blankImage)
        self.labelPile4.grid(row=0, column=3, padx=8, pady=8)
