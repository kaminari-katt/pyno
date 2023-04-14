# Code for both human and bot players

class Player:
  def __init__(self,id,nature,hand):
    self.id = id     # Var for identifying player
    self.nature = nature # =true for human, =false for bot
    self.hand = hand #List of cards...To be broadcast to and from distributor

  def playCard(indexOfCard):
    card = self.hand[indexOfCard] #The card (string) played
    self.hand.remove(card)
    
  def displayCard():
    print(self.hand) #Can be modified to a func if gui is added

  def penalty(penaltyType):
    pass #This part of game logic must be described by the distributor and applied by individual player

  