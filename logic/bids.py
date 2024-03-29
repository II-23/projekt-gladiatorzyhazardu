bids = {
	'high card': {
		'high nine'				:	"High(self.deck.dealt, 'nine')",
		'high ten'				:	"High(self.deck.dealt, 'ten')",
		'high jack'				:	"High(self.deck.dealt, 'jack')",
		'high queen'			:	"High(self.deck.dealt, 'queen')",
		'high king'				:	"High(self.deck.dealt, 'king')",
		'high ace'				:	"High(self.deck.dealt, 'ace')",
	},
	'pair': {
		'pair nine'				:	"Pair(self.deck.dealt, 'nine')",
		'pair ten'				:	"Pair(self.deck.dealt, 'ten')",
		'pair jack'				:	"Pair(self.deck.dealt, 'jack')",
		'pair queen'			:	"Pair(self.deck.dealt, 'queen')",
		'pair king'				:	"Pair(self.deck.dealt, 'king')",
		'pair ace'				:	"Pair(self.deck.dealt, 'ace')",    
	},
	'straight': {
		'low straight'			:	'LowStraight(self.deck.dealt)',
		'high straight'			:	'HighStraight(self.deck.dealt)',		
	},
	'three of a kind': {
		'three nine'			:	"Three(self.deck.dealt, 'nine')",
		'three ten'				:	"Three(self.deck.dealt, 'ten')",
		'three jack'			:	"Three(self.deck.dealt, 'jack')",
		'three queen'			:	"Three(self.deck.dealt, 'queen')",
		'three king'			:	"Three(self.deck.dealt, 'king')",
		'three ace'				:	"Three(self.deck.dealt, 'ace')",    
	},
	'full house': {
		'full nine on ten'		:	"Full(self.deck.dealt, 'nine', 'ten')",
		'full nine on jack'		:	"Full(self.deck.dealt, 'nine', 'jack')",
		'full nine on queen'	:	"Full(self.deck.dealt, 'nine', 'queen')",
		'full nine on king'		:	"Full(self.deck.dealt, 'nine', 'king')",
		'full nine on ace'		:	"Full(self.deck.dealt, 'nine', 'ace')",
		'full ten on nine'		:	"Full(self.deck.dealt, 'ten', 'nine')",
		'full ten on jack'		:	"Full(self.deck.dealt, 'ten', 'jack')",
		'full ten on queen'		:	"Full(self.deck.dealt, 'ten', 'queen')",
		'full ten on king'		:	"Full(self.deck.dealt, 'ten', 'king')",
		'full ten on ace'		:	"Full(self.deck.dealt, 'ten', 'ace')",
		'full jack on nine'		:	"Full(self.deck.dealt, 'jack', 'nine')",
		'full jack on ten'		:	"Full(self.deck.dealt, 'jack', 'ten')",
		'full jack on queen'	:	"Full(self.deck.dealt, 'jack', 'queen')",
		'full jack on king'		:	"Full(self.deck.dealt, 'jack', 'king')",
		'full jack on ace'		:	"Full(self.deck.dealt, 'jack', 'ace')",
		'full queen on nine'	:	"Full(self.deck.dealt, 'queen', 'nine')",
		'full queen on ten'		:	"Full(self.deck.dealt, 'queen', 'ten')",
		'full queen on jack'	:	"Full(self.deck.dealt, 'queen', 'jack')",
		'full queen on king'	:	"Full(self.deck.dealt, 'queen', 'king')",
		'full queen on ace'		:	"Full(self.deck.dealt, 'queen', 'ace')",
		'full king on nine'		:	"Full(self.deck.dealt, 'king', 'nine')",
		'full king on ten'		:	"Full(self.deck.dealt, 'king', 'ten')",
		'full king on jack'		:	"Full(self.deck.dealt, 'king', 'jack')",
		'full king on queen'	:	"Full(self.deck.dealt, 'king', 'queen')",
		'full king on ace'		:	"Full(self.deck.dealt, 'king', 'ace')",
		'full ace on nine'		:	"Full(self.deck.dealt, 'ace', 'nine')",
		'full ace on ten'		:	"Full(self.deck.dealt, 'ace', 'ten')",
		'full ace on jack'		:	"Full(self.deck.dealt, 'ace', 'jack')",
		'full ace on queen'		:	"Full(self.deck.dealt, 'ace', 'queen')",
		'full ace on king'		:	"Full(self.deck.dealt, 'ace', 'king')",    
	},
	'flush': {
		'flush clubs'			:	"Flush(self.deck.dealt, 'clubs')",
		'flush diamonds'		:	"Flush(self.deck.dealt, 'diamonds')",
		'flush hearts'			:	"Flush(self.deck.dealt, 'hearts')",
		'flush spades'			:	"Flush(self.deck.dealt, 'spades')",        
	},
	'four of a kind': {
		'four nine'				:	"Four(self.deck.dealt, 'nine')",
		'four ten'				:	"Four(self.deck.dealt, 'ten')",
		'four jack'				:	"Four(self.deck.dealt, 'jack')",
		'four queen'			:	"Four(self.deck.dealt, 'queen')",
		'four king'				:	"Four(self.deck.dealt, 'king')",
		'four ace'				:	"Four(self.deck.dealt, 'ace')",
	},
	'pokor': {
		'poker clubs'			:	"Poker(self.deck.dealt, 'clubs')",
		'poker diamonds'		:	"Poker(self.deck.dealt, 'diamonds')",
		'poker hearts'			:	"Poker(self.deck.dealt, 'hearts')",
		'poker spades'			:	"Poker(self.deck.dealt, 'spades')",		
	},
	'royale pokor': {
		'king poker clubs'		:	"PokerKing(self.deck.dealt, 'clubs')",
		'king poker diamonds'	:	"PokerKing(self.deck.dealt, 'diamonds')",
		'king poker hearts'		:	"PokerKing(self.deck.dealt, 'hearts')",
		'king poker spades'		:	"PokerKing(self.deck.dealt, 'spades')"        
	}
}

call_bids = { i:bids[j][i] for j in bids for i in bids[j] }

# check whether bid1 is bigger than bid2
def compare_bids(bid1, bid2) -> bool:
    inside = False
    for some_bid in call_bids.keys():
        if some_bid == bid1:
            inside = True
    
    if inside == False:
        return False

    for some_bid in call_bids.keys():
        if some_bid == bid1:
            return False
        
        if some_bid == bid2:
            return True
    return False