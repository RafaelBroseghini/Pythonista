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
        
    def __lt__(self, other):
        card1 = self._suit, self._rank
        card2 = other._suit, other._rank
        return card1 < card2      
    
    def __eq__(self, other):
        if isinstance(other, Card):
            if self._rank == other._rank and self._suit == other._suit:
                return True
            else:
                return False
    
    def __str__(self):
            return str(self._rank) + ' of ' + str(self._suit)
       
