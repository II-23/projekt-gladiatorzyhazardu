from cards import *


class Player:
    
    def __init__(self,number_of_cards, player_id):
        self.losses = 0
        self.active = True
        self.cards_on_hand = set({})
        self.number_of_cards = number_of_cards
        self.id = player_id

