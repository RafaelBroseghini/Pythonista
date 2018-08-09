class Player(object):
  def __init__(self, name):
    self.name = name
    self._hand = []
    
  def get_hand(self):
    return self._hand

  def draw(self, deck):
    drawn_card = deck.pop()
    self._hand.append(drawn_card)
  
  def play_card(self):
    return self._hand.pop()

  def __str__(self):
    return "{}".format(self.name)
