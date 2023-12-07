from enum import IntEnum

Suit={
    "spades"  : 3,
    "hearts"  : 2,
    "diamonds": 1,
    "clubs"   : 0
}

Figures={
    "ace"   : 13,
    "king"  : 12,
    "queen" : 11,
    "ten"   : 10,
    "nine"  : 9
}
 

class Card():
    # figure=""
    # suit=""
    def __init__(self,fig,su):
        self.figure=fig
        self.suit=su
        
def Cardval(card):  #fuction to return pair of values of cards 
    try:
        return(Figures[str(card.figure)],Suit[str(card.suit)])
    except:
        print("TY durniu nie tak!!!!!")