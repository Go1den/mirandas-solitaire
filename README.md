# mirandas-solitaire
Miranda's Solitaire is a solitaire game using two decks of cards. The aim of the game is to move all of the cards into 8 piles. Each scoring pile is suited. For each suit, one pile counts upwards from Ace to King, and the other pile counts down from King to Ace. You can play any visible card at any time, as long as it is the next card in line. When you run out of cards to play, you can draw from the deck. The number of the card you draw determines which play area pile you gain full access to. All of the cards in that pile are then playable until you draw another card. When the deck runs out of cards, you can click "Close Last Pile" to move to the endgame. In the endgame, you have the ability to move cards across the scoring piles, but you can no longer open up any of the play area piles.

Supposedly this is based on a real solitaire game. I can't find any documentation on what the real name of the game is. It also seems to be very difficult in my experience.

This game was coded entirely in Python using tkinter for graphical display. The code is open source and should prove to be a decent teacher of tkinter if you're interested in learning.
