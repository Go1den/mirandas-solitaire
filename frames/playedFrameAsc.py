from tkinter import Frame, Label

from PIL import ImageTk, Image

class PlayedFrameAsc:
    def __init__(self, parent):
        self.frame = Frame(parent.window)
        self.parent = parent

        self.loHeartImage = ImageTk.PhotoImage(Image.open("cards/0H.png"))
        self.loDiamondImage = ImageTk.PhotoImage(Image.open("cards/0D.png"))
        self.loClubImage = ImageTk.PhotoImage(Image.open("cards/0C.png"))
        self.loSpadeImage = ImageTk.PhotoImage(Image.open("cards/0S.png"))

        self.labels = {}

        self.labelPile1 = None
        self.labelPile2 = None
        self.labelPile3 = None
        self.labelPile4 = None

        self.initializeFrame()

    def initializeFrame(self):
        self.labelPile1 = Label(self.frame, image=self.loHeartImage)
        self.labelPile1.grid(row=0, column=0, padx=8, pady=8)
        self.labelPile2 = Label(self.frame, image=self.loDiamondImage)
        self.labelPile2.grid(row=0, column=1, padx=8, pady=8)
        self.labelPile3 = Label(self.frame, image=self.loClubImage)
        self.labelPile3.grid(row=0, column=2, padx=8, pady=8)
        self.labelPile4 = Label(self.frame, image=self.loSpadeImage)
        self.labelPile4.grid(row=0, column=3, padx=8, pady=8)

    def updateAllImages(self):
        self.labelPile1.configure(image=self.parent.playArea.scorePiles["ascH"][-1].image)
        self.labelPile2.configure(image=self.parent.playArea.scorePiles["ascD"][-1].image)
        self.labelPile3.configure(image=self.parent.playArea.scorePiles["ascC"][-1].image)
        self.labelPile4.configure(image=self.parent.playArea.scorePiles["ascS"][-1].image)
