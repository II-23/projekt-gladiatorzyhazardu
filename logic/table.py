# helps to describe current state of game,
# has functions to:
# -randomize cards for every active player for newturn
# -get information about every player
from deck_of_cards import *
from cards import *
from setcheck import *
from player import *

class Table:    
    ##Aliaksander's code from game_start.py with some minor tweaks and made into an init\/\/\/\/\/\/\
    def __init__(self,number_of_players):    
        
        self.players=[]
        self.RecentBid=""
        self.deck=Deck()

        if number_of_players <= 2:
            number_of_cards = 3
        elif number_of_players <= 4:
            number_of_cards = 2
        else: number_of_cards = 1
    
        for i in range(number_of_players):
            self.players.append(Player(number_of_cards))
            for _ in range(number_of_cards):
                self.players[i].cards_on_hand.add(self.deck.get_card())

    def newTurn(self):
        self.deck=Deck()
        self.RecentBid=""
        for player in self.players:
            if player.active:
                player.cards_on_hand=set({})
                for _ in range(player.number_of_cards):
                    player.cards_on_hand.add(self.deck.get_card())

    # def newTurn(self)

#Testing\/\/\/\/\/\/\/\/\/\/
t=Table(2)
for p in t.players:
    print(p.cards_on_hand)
t.newTurn()
print()
for p in t.players:
    print(p.cards_on_hand)