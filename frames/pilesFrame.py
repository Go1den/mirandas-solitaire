from tkinter import Frame, Label

from PIL import ImageTk, Image

class PilesFrame:
    def __init__(self, parent):
        self.frame = Frame(parent.window)
        self.parent = parent

        self.blankImage = ImageTk.PhotoImage(Image.open("cards/red_back.png"))

        self.labelPile1 = None
        self.labelPile2 = None
        self.labelPile3 = None
        self.labelPile4 = None
        self.labelPile5 = None
        self.labelPile6 = None
        self.labelPile7 = None
        self.labelPile8 = None
        self.labelPile9 = None
        self.labelPile10 = None
        self.labelDrawPile = None
        self.labelPile11 = None
        self.labelPile12 = None
        self.labelPile13 = None

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
        self.labelPile5 = Label(self.frame, image=self.blankImage)
        self.labelPile5.grid(row=0, column=4, padx=8, pady=8)
        self.labelPile6 = Label(self.frame, image=self.blankImage)
        self.labelPile6.grid(row=0, column=5, padx=8, pady=8)
        self.labelPile7 = Label(self.frame, image=self.blankImage)
        self.labelPile7.grid(row=0, column=6, padx=8, pady=8)

        self.labelPile8 = Label(self.frame, image=self.blankImage)
        self.labelPile8.grid(row=1, column=0, padx=8, pady=8)
        self.labelPile9 = Label(self.frame, image=self.blankImage)
        self.labelPile9.grid(row=1, column=1, padx=8, pady=8)
        self.labelPile10 = Label(self.frame, image=self.blankImage)
        self.labelPile10.grid(row=1, column=2, padx=8, pady=8)
        self.labelDrawPile = Label(self.frame, image=self.blankImage)
        self.labelDrawPile.grid(row=1, column=3, padx=8, pady=8)
        self.labelPile11 = Label(self.frame, image=self.blankImage)
        self.labelPile11.grid(row=1, column=4, padx=8, pady=8)
        self.labelPile12 = Label(self.frame, image=self.blankImage)
        self.labelPile12.grid(row=1, column=5, padx=8, pady=8)
        self.labelPile13 = Label(self.frame, image=self.blankImage)
        self.labelPile13.grid(row=1, column=6, padx=8, pady=8)