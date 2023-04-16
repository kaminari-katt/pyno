# Code for both human and bot players

import gameLogic as gL

#Characteristics of a playable character

class Player:
  def __init__(self,Id,Nature,Hand):
    self.id = Id     # Var for identifying player
    self.nature = Nature # =true for human, =false for bot
    self.hand = Hand #List of cards...To be broadcast to and from distributor

  def playCard(self,indexOfCard):
    card = self.hand[indexOfCard] #The card (string) played
    self.hand.remove(card)
    
  def displayHand(self):
    print(self.hand) #Can be modified to a func if gui is added

  def penalty(self,penaltyType):
    pass #This part of game logic must be described by the distributor and applied by individual player

#Creation of human players
listOfPlayers = [Player(i,True,gL.players[i]) for i in range(gL.numberOfHumanPlayers)]
