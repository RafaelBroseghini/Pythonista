class Card(object):
    conversion_dict = {"T": "10", "J":"Joker", "Q": "Queen", "K": "King"}

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
            return ['spades','clubs','diamonds','hearts'].index(self._suit) > ['spades','clubs','diamonds','hearts'].index(other._suit) 
        
    def __lt__(self, other):
      if self._suit == other._suit:
        return '23456789TJQKA'.index(self._rank) < '23456789TJQKA'.index(other._rank)
      if self._rank == other._rank:
        return ['spades','clubs','diamonds','hearts'].index(self._suit) < ['spades','clubs','diamonds','hearts'].index(other._suit) 
    
    def __eq__(self, other):
        if isinstance(other, Card):
            if self._rank == other._rank and self._suit == other._suit:
                return True
            else:
                return False
    
    def __str__(self):
      if self._rank in self.conversion_dict:
        return "{} of {}".format(self.conversion_dict[self._rank], self._suit)
      return "{} of {}".format(self._rank, self._suit)
