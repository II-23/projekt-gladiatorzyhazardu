from player import *
from cards import *
from deck_of_cards import *

deck = Deck()
def game_start(number_of_players):

    #deck = Deck()
    
    players=[]
    #number_of_cards
    
    if number_of_players <= 2:
        number_of_cards = 3
    elif number_of_players <= 4:
        number_of_cards = 2
    else: number_of_cards = 1
    
    for i in range(number_of_players):
        players.append(Player())
        for _ in range(number_of_cards):
             players[i].cards_on_hand.add(deck.get_card())

def newTurn(number_of_players): # do wywołania po checku jeśli dobrze myślę; od game_start różni się tylko tym, że nie tworzy się nowych graczy, a zmienia starych
    deck = Deck() # tworzymy nową talię

    if number_of_players <= 2:
        number_of_cards = 3
    elif number_of_players <= 4:
        number_of_cards = 2
    else: number_of_cards = 1

    for i in range(number_of_players):
        players[i].cards_on_hand = set() 
        for _ in range(number_of_cards + players[i].losses): # gracz dostaje dodatkową kartę za każdą przegraną
            players[i].cards_on_hand.add(deck.get_card())
            # CO SIĘ DZIEJE KIEDY KART ZA MAŁO W TALII? SKIPUJE?

#game_start(2)
#deck.print_deck()
