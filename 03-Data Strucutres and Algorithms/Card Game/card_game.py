import random
from card import Card
from player import Player

def build_deck():
  ranks = '23456789TJQKA'
  suits = ['spades','clubs','diamonds','hearts']

  return [Card(r,s) for r in ranks for s in suits]

def shuffle_deck(deck):
  random.shuffle(deck) 

def set_up():
  deck = build_deck()
  shuffle_deck(deck)
  return deck

def check_game_cap(arr):
  if len(arr) < 2:
    raise Exception("Too few players.")
  elif len(arr) > 13:
    raise Exception("Too many players!")

def all_empty_hands(players_array):
  total = len(players_array)

  for p in players_array:
    if len(p.get_hand()) == 0:
      total -= 1
  
  return total == 0

def deal_cards(deck, players):
  for turn in range(4):
    for player in players:
      player.draw(deck)

def game(deck, players = [Player("John Doe"), Player("Ada Lovelace")]):
  score = {str(name):0 for name in players}
  check_game_cap(players)
  deal_cards(deck, players)

  while True:
    round_winner_card = players[0].get_hand()[-1]
    round_winner_player = players[0]
    for player in range(len(players)):
      choice = players[player].play_card()
      if choice > round_winner_card:
        round_winner_card = choice
        round_winner_player = players[player]
    score[str(round_winner_player)] += 1
    # compute winner for that round.

    if len(deck) == 0:
      if all_empty_hands(players):
        #check_all_hands and length of deck.
        return score

    if len(deck) > 0:
      for player in players:
        player.draw(deck)

  return max(score)

def main():
  deck = set_up()
  final_score = game(deck)
  print(final_score)

if __name__ == "__main__":
  main()
