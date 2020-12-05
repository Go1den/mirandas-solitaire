import sys
from tkinter import Tk, Frame, Menu, W, E

from frames.pilesFrame import PilesFrame
from frames.playedFrameAsc import PlayedFrameAsc
from frames.playedFrameDesc import PlayedFrameDesc

class MainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.playedFrameAsc = PlayedFrameAsc(self)
        self.playedFrameDesc = PlayedFrameDesc(self)
        self.pilesFrame = PilesFrame(self)
        self.currentPileFrame = Frame(self.window)

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
        self.playedFrameAsc.frame.grid(row=0, column=0, sticky=W)
        self.playedFrameDesc.frame.grid(row=0, column=1, sticky=E)
        self.pilesFrame.frame.grid(row=1, column=0, columnspan=2)
        self.currentPileFrame.grid(row=2, column=0, columnspan=2)

    def addMenu(self):
        menu = Menu(self.window)

        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="Quit", command=lambda: self.closeWindow())
        menu.add_cascade(label="File", menu=fileMenu)

        self.window.config(menu=menu)

    def closeWindow(self):
        sys.exit(0)

