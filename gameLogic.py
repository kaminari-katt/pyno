# main Game Logic


import random

numberOfHumanPlayers = 4

# --- DATA ---
zeroes = 4
ones = 8
twos = 8
threes = 8
fours = 8
fives = 8
sixes = 8
sevens = 8
eights = 8
nines = 8
skips = 8
reverses = 8
plusTwos = 8
plusFours = 4 # no colors
wildCards = 4 # no colors
# --- DATA ---

# card types, double entries are for 8 cards, 4 cadds for each color two times is 8 cards.
cardTypes = ["0", "1", "1", "2", "2", "3","3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "Skip", "Skip", "Reverse", "Reverse", "+2", "+2", "+4", "W"]
colors = ["R", "Y", "B", "G"]

# cards in each players hand
playerOneHand = []
playerTwoHand = []
playerThreeHand = []
playerFourHand = []
# list for code comfortability in looping
players = [playerOneHand, playerTwoHand, playerThreeHand, playerFourHand]

cards = [] # the cards in the deck

# shuffle the cards and place them in deck
def gameShuffle():
    for cardType in cardTypes:
        for color in colors:
            cards.append(f"{color}{cardType}")
    random.shuffle(cards)        

gameShuffle()
print(cards)

# serve 7 cards for each player one by one
def distribute():
    for i in range(0,7):
        for player in players:
            player.append(cards[0])
            cards.remove(cards[0])

# gameShuffle()
distribute()
# print(cards)
print(players)