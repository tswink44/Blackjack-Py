import random
from functions import initializeDeck,dealhand,translatehand,calculatehandpoints,IsBust
from classes import Card

#Initializng deck and possible suits and cardnums/points (2,8,J,etc.,)
deck = []
suitlist = [1,2,3,4]
cardnumlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
pointslist = [11,2,3,4,5,6,7,8,9,10,10,10,10]


#Initializes deck to start game
deck = initializeDeck(suitlist,cardnumlist,deck)
#Takes player name
playername = input("Let's Play Blackjack! What's your name?\n")
print("Dealing cards...")
#Deals hands and then calculates points
playerhand = []
dealerhand = []
playerhand = dealhand(deck)
dealerhand = dealhand(deck)
playerpoints = calculatehandpoints(playerhand)
dealerpoints = calculatehandpoints(dealerhand)
#Announces hands of player and ealer
print("Your hand is a " + translatehand(playerhand))
print("Dealer hand is a " + translatehand(dealerhand))


#Main gameplay loop for player
while playerpoints <= 21:
    #Checks if player input for move is valid
    validMove = False
    while validMove == False:
        move = input("Hit or Stand? Press 1 for Hit or 2 for Stand")
        if move == str(1) or move == str(2):
            break
        else:
            validMove == False
            print("Invalid move, please input again")
    #If a user stands, break while loop
    if move == str(2):
        break
    if move == str(1):
        #draws a random card from the remaining deck
        randomint = random.randint(0,len(deck)-1)
        playerhand.append(deck.pop(randomint))
        #calculates player points
        playerpoints = calculatehandpoints(playerhand)
        #If bust, announces it
        if IsBust(playerpoints) == True:
            print("Player Busts :(")
            break
        print ("Your new hand is a " + translatehand(playerhand))
        



