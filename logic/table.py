# helps to describe current state of game,
# has functions to:
# -randomize cards for every active player for nextTurn
# -get information about every player
from logic.deck_of_cards import *
from logic.cards import *
from logic.setcheck import *
from logic.player import *

class Table:    
    ##Aliaksander's code from game_start.py with some minor tweaks and made into an init\/\/\/\/\/\/\
    def __init__(self):
        self.players=[]
        self.recent_bid=""
        self.deck=Deck()
        self.current_index = 0
        self.started = False

    def addPlayer(self, new_player):
        self.players.append(new_player)

    def removePlayer(self, player):
        for i in range(self.players):
            if self.players[i].id == player.id:
                self.players.pop(i)
                return True
        return False

    def startGame(self):
        for i in range(len(self.players)):
            self.players[i].cards_on_hand.add(self.deck.get_card())
            self.players[i].active = True

        self.started = True
        self.nextTurn()

    def nextTurn(self):
        if len(self.players) == 1:
            self.started = False
            return

        self.deck = Deck()
        self.recent_bid = ""

        max_number_of_cards = min(6, 23 / len(self.players))

        for i in range(len(self.players)):
            if self.players[i].losses + 1 > max_number_of_cards:
                self.players[i].active = False
            
            self.players[i].cards_on_hand = set({})
            if self.players[i].active == True:
                for _ in range(self.players[i].losses + 1):
                    self.players[i].cards_on_hand.add(self.deck.get_card())

    def getCurrentPlayer(self):
        if len(self.players) == 0:
            return -1
        return self.players[self.current_index].id
    
    def play(self, bid):
        if bid == "Check":
            if eval(self.recent_bid) == True:
                self.players[self.current_index].losses += 1
            else:
                previous_player = (self.current_index + len(self.players) - 1) % len(self.players)
                self.players[previous_player].losses += 1
            
            self.nextTurn()
        else:
            self.recent_bid = bid
            self.current_index = (self.current_index + 1) % len(self.players)

#Testing\/\/\/\/\/\/\/\/\/\/


if __name__ == '__main__':
    t = Table()
    player1 = Player(2, "123123")
    player2 = Player(3, "131233")

    t.addPlayer(player1)
    t.addPlayer(player2)

    t.startGame()

    for p in t.players:
        print(p.cards_on_hand)
    t.nextTurn()
    print()
    for p in t.players:
        print(p.cards_on_hand)