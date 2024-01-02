from deck_of_cards import *
from cards import *
from setcheck import *
from player import *

def check(curr_player, prev_player): # obecny gracz sprawdza poprzedniego
	curr_bid = eval(RecentBid) # zamienia string postaci np "Pair(deck, 'hearts')" na funkcję, wtedy wywołanie tego w ifie zwróci wynik
	if curr_bid: # jeśli check przechodzi
		curr_player.losses += 1
	else: # check nie przechodzi
		prev_player.losses += 1

# --------TEST--------
"""
deck = Deck() #robimy sztuczną talię z czterema królami i dziesiątkami
for i in range(4):
	deck.dealt.add(Card( 13, i ))
	deck.dealt.add(Card( 10, i ))
#print(deck.dealt)
A = Player()
B = Player()
RecentBid = "Full(deck.dealt, 'king', 'ten')" # patrzymy w deck.dealt, czyli wszystkich rozdanych kartach w tej turze
check(A, B) # A sprawdza B; bid powinien przejść, więc A.losses == 1 (tak powinno być)
print(A.losses)
RecentBid = "Poker(deck.dealt, 'diamonds')"
check(B, A) # B sprawdza A; nie powinien przejść, ostateczny wynik A.losses 2 : 0 B.losses
print(A.losses, B.losses)
"""