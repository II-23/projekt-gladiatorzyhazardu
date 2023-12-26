from cards import *
import random

class Deck:

    # cards=set()
    # dealt=set()
    
    def add(self,card):
        self.cards.add(card)
           
    def __init__(self):
        
        self.cards=set()
        self.dealt=set()

        for i in range(4):
            for j in range(9,15):
                self.add(Card(j, i))
                
    def print_deck(self):
        for i in self.cards:
            print(i)
        print(len(self.cards))
    
    def get_card(self):
        cur_card = random.choice(tuple(self.cards))
        self.cards.remove(cur_card)
        self.dealt.add(cur_card)
        return cur_card



#----------------TESTING----------------------#
# a=Deck()
# print(a.get_card())
# a.print_deck()