from logic.cards import *
import time

import json

class Player:
    
    def __init__(self, player_id, nickname):
        self.nickname = nickname
        self.losses = 0
        self.active = True
        self.cards_on_hand = set({})
        self.number_of_cards = 0
        self.id = player_id
        self.table_id = -1
        self.last_ping = time.time()
    
    def joining_table(self, table_id):
        self.losses = 0
        self.table_id = table_id