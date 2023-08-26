import random
#Class for card objects
class Card:
    def __init__(self,suit,cardnum):
        self.suit = suit
        self.cardnum = cardnum

#Initializng deck and possible suits and cardnums/points (2,8,J,etc.,)
deck = []
suitlist = [1,2,3,4]
cardnumlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
pointslist = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def initializeDeck(suitlist,cardlist,decklist):
    for suit in suitlist:
        for card in cardlist:
            decklist.append(Card(suit,card))
    return decklist
#Deals hands for player and dealer
def dealhand(deck):
    hand = []
    randint1 = random.randint(0,len(deck)-1)
    randint2 = random.randint(0,len(deck)-1)
    while randint1 == randint2:
        randint2 = random.randint(0,len(deck)-1)
    hand.append(deck.pop(randint1))
    hand.append(deck.pop(randint2))
    return hand
#Translate hand into human (instead of [11,3] its Jack of Hearts)
def translatehand(hand):
    transuit = []
    transcard = []
    for card in hand:
        suit = card.suit
        cardnum = card.cardnum
        if suit == 1:
            transuit.append("Spades")
        elif suit == 2:
            transuit.append("Clubs")
        elif suit == 3:
            transuit.append("Hearts")
        else:
            transuit.append("Diamonds")
        if cardnum == 1:
            transcard.append("Ace")
        elif cardnum == 11:
            transcard.append("Jack")
        elif cardnum == 12:
            transcard.append("Queen")
        elif cardnum == 13:
            transcard.append("King")
        else:
            transcard.append(cardnum)
    
    return "Your cards are {cards} of suits {suits}".format(cards = transcard, suits = transuit)
    
#Calculate points for a hand
def calculatehandpoints(hand):
    points = 0
    hasAce = False
    for card in hand:
        if card.cardnum == 1:
            hasAce = True
        cardnum = card.cardnum -1
        points += pointslist[cardnum]
    #If a hand has an Ace and busts using 11 points, instead using 1 point
    if hasAce == True and points > 21:
        points = points - 10
    return points
#Determines if hand is bust
def IsBust(points):
    if points > 21:
        return True
    else:
        return False


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
        



