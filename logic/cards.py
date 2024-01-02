from enum import IntEnum

Suit={
    3   :   "spades",
    2   :   "hearts",
    1   :   "diamonds",
    0   :   "clubs",
}

Figures={
    14  :   "ace",
    13  :   "king",
    12  :   "queen",
    11  :   "jack",
    10  :   "ten",
    9   :   "nine"
}
 

class Card():
    # figure=""
    # suit=""
    def __init__(self,fig,su):
        self.figure=Figures[fig]
        self.suit=Suit[su]

    def __repr__(self):
        return f'{self.figure} of {self.suit}'
        
def Cardval(card):  #fuction to return pair of values of cards 
    try:
        return(Figures[int(card.figure)],Suit[int(card.suit)])
    except:
        print("TY durniu nie tak!!!!!")