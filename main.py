from deck import Deck
from mainWindow import MainWindow

mainWindow = MainWindow()

# Proving that save/load seed is working
# deck = Deck()
# deck.shuffle()
# print(deck.getSeed())
# deck.loadSeed(deck.getSeed())
# print(deck.getSeed())

mainWindow.window.mainloop()
