from tkinter import Frame, Label, Toplevel, Button, E

from windows.windowHelper import WindowHelper

class EndOfDrawPileWindow:
    def __init__(self, parent):
        self.window = Toplevel(parent.window)
        self.window.withdraw()
        self.parent = parent

        self.frame = Frame(self.window)
        self.gridFrames()

        WindowHelper.initializeWindow(self.window, self.parent, 260, 70, 284, 320, "Draw pile exhausted.")
        self.populateFrame()
        WindowHelper.finalizeWindow(self.window, self.parent)

    def gridFrames(self):
        self.frame.grid(row=0, padx=4, pady=4)

    def populateFrame(self):
        label = Label(self.frame, text="You may now move cards across the top row.")
        label.grid(row=0, padx=4, pady=4)
        okButton = Button(self.frame, text="OK", command=self.close, width=8)
        okButton.grid(row=1, padx=4, pady=4, sticky=E)

    def close(self):
        self.window.destroy()
