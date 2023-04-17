# Code for both human and bot players

import gameLogic

#Characteristics of a playable character

class Player:
  def __init__(self,Id,Nature,Hand):
    self.id = Id     # Var for identifying player
    self.nature = Nature # =true for human, =false for bot
    self.hand = Hand #List of cards...To be broadcast to and from distributor

  def playCard(self,indexOfCard):
    card = self.hand[indexOfCard] #The card (string) played
    self.hand.remove(card)
    return card
    
  def displayHand(self):
    return self.hand #Can be modified to a func if gui is added
    
  def penalty(self,penaltyType):
  #Le I think this whole method should be implemented on gameLogic file because removit card from deck should not be a work of player....
    if penaltyType == "+2":
      for t in range(0,1):
        self.hand.append(gameLogic.cards[0])
        gameLogic.cards.remove(cards[0])
       
    if penaltyType == "+4":
      for t in range(0,3):
        self.hand.append(gameLogic.cards[0])
        gameLogic.cards.remove(cards[0])

#Creation of human players
listOfPlayers = [Player(i,True,gameLogic.players[i]) for i in range(gameLogic.numberOfHumanPlayers)]
