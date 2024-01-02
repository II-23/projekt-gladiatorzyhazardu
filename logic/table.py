# helps to describe current state of game,
# has functions to:
# -randomize cards for every active player for newturn
# -get information about every player
from logic.deck_of_cards import *
from logic.cards import *
from logic.setcheck import *
from logic.player import *

class Table:    
    ##Aliaksander's code from game_start.py with some minor tweaks and made into an init\/\/\/\/\/\/\
    def __init__(self):
        self.players=[]
        self.RecentBid=""
        self.deck=Deck()

    def addPlayer(self, new_player):
        self.players.append(new_player)

    def removePlayer(self, player):
        for i in range(self.players):
            if self.players[i].id == player.id:
                self.players.pop(i)
                return True
        return False

    def startGame(self):

        number_of_players = len(self.players)

        if number_of_players <= 2:
            number_of_cards = 3
        elif number_of_players <= 4:
            number_of_cards = 2
        else: 
            number_of_cards = 1
    
        for i in range(number_of_players):
            for _ in range(number_of_cards):
                self.players[i].cards_on_hand.add(self.deck.get_card())

        self.newTurn()

    def newTurn(self):
        self.deck=Deck()
        self.RecentBid=""
        for player in self.players:
            if player.active:
                player.cards_on_hand=set({})
                for _ in range(player.number_of_cards):
                    player.cards_on_hand.add(self.deck.get_card())

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
    t.newTurn()
    print()
    for p in t.players:
        print(p.cards_on_hand)