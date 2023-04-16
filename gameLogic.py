# main Game Logic


import random

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

# card code tokens
cardTypes = ["0", "1", "1", "2", "2", "3","3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "Skip", "Skip", "Reverse", "Reverse", "+2", "+2", "+4", "W"]
colors = ["R", "Y", "B", "G"]

numberOfHumanPlayers = 4

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

# serve 7 cards for each player one by one
def distribute():
    for i in range(0,7):
        for player in players:
            player.append(cards[0])
            cards.remove(cards[0])

# method to translate card codes into strings that is readable
def translate(cardCode):
    if cardCode.startswith("R"):
        color = "Red "
    if cardCode.startswith("Y"):
        color = "Yellow "
    if cardCode.startwith("B"):
        color = "Blue "
    if cardCode.startswith("G"):
        color = "Green "
    if cardCode.endswith("1"):
        cardValue = "One"
    if cardCode.endswith("2"):
        cardValue = "Two"
    if cardCode.endswith("3"):
        cardValue = "Three"
    if cardCode.endswith("4"):
        cardValue = "Four"
    if cardCode.endswith("5"):
        cardValue = "Five"
    if cardCode.endswith("6"):
        cardValue = "Six"
    if cardCode.endswith("7"):
        cardValue = "Seven"
    if cardCode.endswith("8"):
        cardValue = "Eight"
    if cardCode.endswith("9"):
        cardValue = "Nine"
    if cardCode.endswith("Skip"):
        cardValue = "Skip"
    if cardCode.endswith("Reverse"):
        cardValue = "Reverse"
    if cardCode.endswith("+2"):
        cardValue = "Plus Two"
    if cardCode.endswith("+4"):
        cardValue = "Plus Four"
        color = ""
    if cardCode.endswith("W"):
        cardValue = "Wild"
        color = ""
        
    cardName = str(str(color) + str(cardValue) + " Card")
    return cardName

gameShuffle()
distribute()

