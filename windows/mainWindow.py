import sys
from tkinter import Tk, Frame, Menu, EW, NSEW

from deck import Deck
from frames.currentPileFrame import CurrentPileFrame
from frames.pilesFrame import PilesFrame
from frames.playedFrameAsc import PlayedFrameAsc
from frames.playedFrameDesc import PlayedFrameDesc
from playArea import PlayArea

class MainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.deck = None
        self.playArea = None
        self.startNewGame()

        self.playedFrame = Frame(self.window)
        self.playedFrameAsc = PlayedFrameAsc(self)
        self.playedFrameDesc = PlayedFrameDesc(self)
        self.pilesFrame = PilesFrame(self)
        self.currentPileFrame = CurrentPileFrame(self)

        self.initializeWindow()
        self.gridFrames()
        self.addMenu()
        self.window.deiconify()

    def initializeWindow(self):
        # self.window.iconbitmap(FileConstants.STREAMOPENER_ICON)
        self.window.geometry('1280x720')
        self.window.title("Miranda's Solitaire")
        self.window.resizable(width=False, height=False)

    def gridFrames(self):
        self.playedFrameAsc.frame.grid(row=0, column=0, padx=(0, 232), sticky=EW)
        self.playedFrameDesc.frame.grid(row=0, column=1, padx=(232, 0), sticky=EW)
        self.playedFrame.grid(row=0, column=0, padx=4, pady=4, sticky=EW)
        self.pilesFrame.frame.grid(row=1, column=0, padx=4, pady=4, sticky=NSEW)
        self.currentPileFrame.frame.grid(row=2, column=0, padx=4, pady=4, sticky=EW)

    def addMenu(self):
        menu = Menu(self.window)

        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="Quit", command=lambda: self.closeWindow())
        menu.add_cascade(label="File", menu=fileMenu)

        self.window.config(menu=menu)

    def closeWindow(self):
        sys.exit(0)

    def startNewGame(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.playArea = PlayArea(self)
        self.playArea.deal(self.deck)



