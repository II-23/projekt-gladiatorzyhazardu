from logic.deck_of_cards import *
from logic.cards import *
from logic.setcheck import *
from logic.player import *
from logic.bids import *

class Table:

    def __init__(self):
        self.players = []
        self.recent_bid = ""
        self.bid_history = []
        self.deck = Deck()
        self.current_index = 0
        self.started = False
        self.first_player = 0
        self.looser = None

    def addPlayer(self, new_player: Player):
        self.players.append(new_player)

    def removePlayer(self, player_id: int):
        for i in range(len(self.players)):
            if self.players[i].id == player_id:
                self.players.pop(i)
                return True
        return False

    def startGame(self):
        deck = Deck()

        for i in range(len(self.players)):
            self.players[i].losses=0
            self.players[i].cards_on_hand = set({self.deck.get_card()})
            self.players[i].active = True

        self.started = True
        self.nextTurn()
    
    def endGame(self):
        winner = max(self.players, key=lambda x: x.losses, default=None)
        return winner
    
    def nextTurn(self):
        if len(self.players) == 1:
            self.endGame()
            self.startGame()
            return
        
        self.current_index = self.first_player
        self.deck = Deck()
        self.recent_bid = ""
        self.bid_history=[]
        max_number_of_cards = min(6, 23 / len(self.players))
        active_players=0

        for i in range(len(self.players)):
            if self.players[i].losses + 1 > max_number_of_cards:
                self.players[i].active = False

            self.players[i].cards_on_hand = set({})
            if self.players[i].active == True:
                active_players+=1
                for _ in range(self.players[i].losses + 1):
                    self.players[i].cards_on_hand.add(self.deck.get_card())
        
        if(active_players==1): 
            self.endGame()
            self.startGame()
            return
        
        while not self.players[self.current_index].active:
            self.current_index = (self.current_index + 1) % len(self.players)

    def getCurrentPlayer(self):
        if len(self.players) == 0:
            return -1
        return self.players[self.current_index].id
    
    def play(self, player_id, bid):
        
        if self.players[self.current_index].id != player_id:
            return False

        if bid == "check":
            if self.recent_bid == "":
                return False
            
            call = call_bids[self.recent_bid]

            print("call: ", call)
            print("deck: ", self.deck.dealt)

            if eval(call) == True:
                self.players[self.current_index].losses += 1
                self.looser=self.current_index
            else:
                previous_player = (self.current_index + len(self.players) - 1) % len(self.players)
                self.players[previous_player].losses += 1
               
                self.current_index = previous_player
                self.looser=self.current_index

            print("next turn")
            self.first_player = self.current_index
            self.nextTurn()
        else:
            
            if len(self.bid_history) > 0 and compare_bids(bid, self.bid_history[-1]) == False:
                return False

            self.bid_history.append(bid)
            self.recent_bid = bid
            self.current_index = (self.current_index + 1) % len(self.players)

            while not self.players[self.current_index].active:
                self.current_index = (self.current_index + 1) % len(self.players)
            self.looser=None

        return True

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
    # for p in t.players:
    #     print(p.cards_on_hand)
    # #testing bid-related methods
    # t.AvailableBids()
    # t.play('full ten on queen')
    # t.ShowBidHistory()
    # t.AvailableBids()
    # t.play('flush spades')
    # t.ShowBidHistory()
    # t.AvailableBids()