# helps to describe current state of game,
# has functions to:
# -randomize cards for every active player for nextTurn
# -get information about every player
from logic.deck_of_cards import *
from logic.cards import *
from logic.setcheck import *
from logic.player import *
from logic.bids import *

class Table:
    ##Aliaksander's code from game_start.py with some minor tweaks and made into an init\/\/\/\/\/\/\
    def __init__(self):
        self.players=[]
        self.recent_bid=""
        self.bid_history=[]
        self.deck=Deck()
        self.current_index = 0
        self.started = False
        self.first_player=0

    def addPlayer(self, new_player):
        self.players.append(new_player)

    def removePlayer(self, player_id):
        for i in range(self.players):
            if self.players[i].id == player_id:
                self.players.pop(i)
                return True
        return False

    def startGame(self):
        for i in range(len(self.players)):
            self.players[i].cards_on_hand.add(self.deck.get_card())
            self.players[i].active = True

        self.started = True
        self.nextTurn()
    
    def endGame(self):
        winner = max(self.players, key=lambda x: x.losses, default=None)
        return winner
    
    def nextTurn(self):
        if len(self.players) == 1:
            self.started = False
            return
        self.current_index=self.first_player #set current player to player which starts that turn
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

    def AvailableBids(self):
        cont = False
        print("'check' is always available")
        print('Your current options are:')
        if self.recent_bid == '':
            cont = True
        for i in disp_bids:
            if self.recent_bid in disp_bids[i]:
                cont = True
            if cont and self.recent_bid != list(disp_bids[i].keys())[-1]:
                print(i)
        opt = input('\nInput which available bids to show:\n')
        print(f'\nFrom bids of type {opt} you can choose:')
        if self.recent_bid not in disp_bids[opt]:
            for i in disp_bids[opt]:
                print(i)
        else:
            cont = False
            for i in disp_bids[opt]:
                if cont:
                    print(i)
                if self.recent_bid == i:
                    cont = True

    def ShowBidHistory(self):
        print('Most recent bid:')
        print(f'\t{self.recent_bid}')
        print('Earlier bids:')
        for i in self.bid_history[::-1]:
            print(f'\t{i}')
    
    def play(self, bid):
        if bid == "check":
            call = call_bids[self.recent_bid]
            if eval(call) == True:
                self.players[self.current_index].losses += 1
            else:
                previous_player = (self.current_index + len(self.players) - 1) % len(self.players)
                self.players[previous_player].losses += 1
               
                self.current_index=previous_player

            self.first_player=self.current_index  #set player which starts first
            self.nextTurn()
        else:
            self.bid_history.append(self.recent_bid)
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
    #testing bid-related methods
    t.AvailableBids()
    t.play('full ten on queen')
    t.ShowBidHistory()
    t.AvailableBids()
    t.play('flush spades')
    t.ShowBidHistory()
    t.AvailableBids()