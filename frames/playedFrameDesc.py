from tkinter import Frame, Label

from PIL import ImageTk, Image

class PlayedFrameDesc:
    def __init__(self, parent):
        self.frame = Frame(parent.window)
        self.parent = parent

        self.hiHeartImage = ImageTk.PhotoImage(Image.open("cards/14H.png"))
        self.hiDiamondImage = ImageTk.PhotoImage(Image.open("cards/14D.png"))
        self.hiClubImage = ImageTk.PhotoImage(Image.open("cards/14C.png"))
        self.hiSpadeImage = ImageTk.PhotoImage(Image.open("cards/14S.png"))

        self.labelPile1 = None
        self.labelPile2 = None
        self.labelPile3 = None
        self.labelPile4 = None

        self.initializeFrame()

    def initializeFrame(self):
        self.labelPile1 = Label(self.frame, image=self.hiHeartImage)
        self.labelPile1.grid(row=0, column=0, padx=8, pady=8)
        self.labelPile2 = Label(self.frame, image=self.hiDiamondImage)
        self.labelPile2.grid(row=0, column=1, padx=8, pady=8)
        self.labelPile3 = Label(self.frame, image=self.hiClubImage)
        self.labelPile3.grid(row=0, column=2, padx=8, pady=8)
        self.labelPile4 = Label(self.frame, image=self.hiSpadeImage)
        self.labelPile4.grid(row=0, column=3, padx=8, pady=8)

    def updateAllImages(self):
        self.labelPile1.configure(image=self.parent.playArea.scorePiles["descH"][-1].image)
        self.labelPile2.configure(image=self.parent.playArea.scorePiles["descD"][-1].image)
        self.labelPile3.configure(image=self.parent.playArea.scorePiles["descC"][-1].image)
        self.labelPile4.configure(image=self.parent.playArea.scorePiles["descS"][-1].image)
