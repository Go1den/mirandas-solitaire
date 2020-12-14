import sys
from tkinter import Tk, Frame, Menu, EW, NSEW, StringVar

from deck import Deck
from frames.currentPileFrame import CurrentPileFrame
from frames.pilesFrame import PilesFrame
from frames.playedFrameAsc import PlayedFrameAsc
from frames.playedFrameDesc import PlayedFrameDesc
from playArea import PlayArea
from windows.aboutWindow import AboutWindow
from windows.howToPlayWindow import HowToPlayWindow

class MainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.deck = None
        self.playArea = None

        self.playedFrame = None
        self.playedFrameAsc = None
        self.playedFrameDesc = None
        self.pilesFrame = None
        self.currentPileFrame = None

        self.deckColor = StringVar()
        self.deckColor.set("cards/red_back.png")

        self.startNewGame()
        self.setFrames()

        self.initializeWindow()
        self.gridFrames()
        self.addMenu()
        self.window.deiconify()

    def initializeWindow(self):
        # self.window.iconbitmap(FileConstants.STREAMOPENER_ICON)
        self.window.geometry('840x650')
        self.window.title("Miranda's Solitaire")
        self.window.resizable(width=False, height=False)

    def setFrames(self):
        self.playedFrame = Frame(self.window)
        self.playedFrameAsc = PlayedFrameAsc(self)
        self.playedFrameDesc = PlayedFrameDesc(self)
        self.pilesFrame = PilesFrame(self)
        self.currentPileFrame = CurrentPileFrame(self)

    def gridFrames(self):
        self.playedFrameAsc.frame.grid(row=0, column=0, padx=4, sticky=EW)
        self.playedFrameDesc.frame.grid(row=0, column=1, padx=4, sticky=EW)
        self.playedFrame.grid(row=0, column=0, padx=4, pady=4, sticky=EW)
        self.pilesFrame.frame.grid(row=1, column=0, padx=(60, 570), pady=4, sticky=NSEW)
        self.currentPileFrame.frame.grid(row=2, column=0, padx=(60, 570), pady=4, sticky=EW)

    def addMenu(self):
        menu = Menu(self.window)

        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="New Game", command=lambda: self.startNewGame())
        fileMenu.add_command(label="Restart Game", command=lambda: self.restartGame())
        fileMenu.add_command(label="Quit", command=lambda: self.closeWindow())
        menu.add_cascade(label="File", menu=fileMenu)

        colorMenu = Menu(menu, tearoff=0)
        colorMenu.add_radiobutton(label="Blue", value="cards/blue_back.png", variable=self.deckColor, command=lambda: self.pilesFrame.setCardBackImage())
        colorMenu.add_radiobutton(label="Gray", value="cards/gray_back.png", variable=self.deckColor, command=lambda: self.pilesFrame.setCardBackImage())
        colorMenu.add_radiobutton(label="Green", value="cards/green_back.png", variable=self.deckColor, command=lambda: self.pilesFrame.setCardBackImage())
        colorMenu.add_radiobutton(label="Purple", value="cards/purple_back.png", variable=self.deckColor, command=lambda: self.pilesFrame.setCardBackImage())
        colorMenu.add_radiobutton(label="Red", value="cards/red_back.png", variable=self.deckColor, command=lambda: self.pilesFrame.setCardBackImage())
        colorMenu.add_radiobutton(label="Yellow", value="cards/yellow_back.png", variable=self.deckColor, command=lambda: self.pilesFrame.setCardBackImage())
        menu.add_cascade(label="Deck Color", menu=colorMenu)

        helpMenu = Menu(menu, tearoff=0)
        helpMenu.add_command(label="How To Play", command=lambda: HowToPlayWindow(self))
        helpMenu.add_command(label="About", command=lambda: AboutWindow(self))
        menu.add_cascade(label="Help", menu=helpMenu)

        self.window.config(menu=menu)

    def closeWindow(self):
        sys.exit(0)

    def startNewGame(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.playArea = PlayArea(self)
        self.playArea.deal(self.deck)
        self.destroyWidgets()
        self.setFrames()
        self.gridFrames()

    def restartGame(self):
        self.playArea = PlayArea(self)
        self.playArea.deal(self.deck)
        self.destroyWidgets()
        self.setFrames()
        self.gridFrames()

    def destroyWidgets(self):
        for widget in self.window.winfo_children():
            if not isinstance(widget, Menu):
                widget.destroy()
