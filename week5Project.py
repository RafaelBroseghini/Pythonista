import random
class Card:
    def __init__(self, rank, suit):
        if rank in '23456789TJQKA':
            self._rank = rank
        else:
            raise ValueError('Invalid rank')
        if suit in ['spades','clubs','diamonds','hearts']:
            self._suit = suit
        else:
            raise ValueError('Invalid suit')
        
    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __gt__(self, other):
        if self._suit == other._suit:
            return '23456789TJQKA'.index(self._rank) > '23456789TJQKA'.index(other._rank)
        if self._rank == other._rank:
            return ['spades','clubs','diamonds','hearts'].index(self._suit) > ['spades','clubs','diamonds','hearts'].index(self._suit)
       
    def __str__(self):
            return str(self._rank) + ' of ' + str(self._suit)    
       

class Deck():
    card_list = []
    def __init__(self):
        self._card_list = card_list
        for s in ['spades','clubs','diamonds','hearts']:
            for r in '23456789TJQKA':
                c = Card(r, s)
        self._card_list.append(c)
    @property    
    def draw(self):
        return self._card_list.pop()
    
    def shuffle(self):
        return random.shuffle(self._card_list)
    
    def __str__(self):
        for i in range(self._card_list):
            return i
        
class Player:
    hand = []
    name = input(' ')
    def __init__(self, name):
        self._name = name
        self._hand = hand
        
    def draw_card(self, deck):
        self._deck = hand.draw(self)
        
    def show_hand(self):
        return str(self._deck)
        
def main():
    print("Let's play a game!")
    main_deck = Deck()
    main_deck.shuffle()
    player1 = Player("Alice", 5)
    player2 = Player("Bob", 5)
    for _ in range(5):
        player1.draw_card(main_deck)
        player2.draw_card(main_deck)
        print(*player1.hand)
        print(*player2.hand)
               
if __name__ == "__main__":
    main()

        