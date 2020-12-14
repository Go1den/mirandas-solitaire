from tkinter import Frame, Label, Toplevel, Button, E, SE, W, LEFT

from windows.windowHelper import WindowHelper

class AboutWindow:
    def __init__(self, parent):
        self.window = Toplevel(parent.window)
        self.window.withdraw()
        self.parent = parent

        self.frame = Frame(self.window)
        self.gridFrames()

        WindowHelper.initializeWindow(self.window, self.parent, 260, 96, 288, 320, "About")
        self.populateFrame()
        WindowHelper.finalizeWindow(self.window, self.parent)

    def gridFrames(self):
        self.frame.grid(row=0, padx=4, pady=4)

    def populateFrame(self):
        label = Label(self.frame, text="Miranda's Solitaire, Version 1.0\nwww.github.com/go1den/mirandas-solitaire", justify=LEFT)
        label.grid(row=0, padx=4, pady=4)
        okButton = Button(self.frame, text="OK", command=self.close, width=8)
        okButton.grid(row=1, padx=4, pady=4, sticky=SE)

    def close(self):
        self.window.destroy()
