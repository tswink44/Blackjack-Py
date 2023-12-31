import random
from classes import Card
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
    randint2 = random.randint(0,len(deck)-2)
    while randint1 == randint2:
        randint2 = random.randint(0,len(deck)-2)
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
    
    return "{cards} of suits {suits}".format(cards = transcard, suits = transuit)
    
#Calculate points for a hand
def calculatehandpoints(hand):
    points = 0
    hasAce = False
    hasTwoAces = False
    for card in hand:
        if card.cardnum == 1:
            if hasAce == True:
                hasTwoAces = True
            else:
                hasAce = True
        cardnum = card.cardnum -1
        points += pointslist[cardnum]
    #If a hand has an Ace and busts using 11 points, instead using 1 point
    if hasAce == True and points > 21:
        points = points - 10
        if points > 21 and hasTwoAces == True:
            points = points -10
    return points
#Determines if hand is bust
def IsBust(points):
    if points > 21:
        return True
    else:
        return False
