import os
import re
import random
import string

class Announcer(object):
  def __init__(self, difficulty={"e":["easy",(3,4)],"i":["intermediate",(5,7)],"h":["hard",(8,12)]}, tries=10):
    self.difficulty = difficulty
    self.tries = tries

  def display_difficulties(self):
    for k,v in self.difficulty.items():
        print("({}): {}".format(k,v[0]))

  def display_supported_difficulties(self):
    print("Hi there! Let's play hangman!")
    print("-"*30+"\n")
    print("First you need to select a difficulty: \n")

    self.display_difficulties()
    
    diff = input("Difficulty: ")
    while diff not in self.difficulty:
        print("{} is not a(n) supported difficulty input. Try again!\n".format(diff))
        self.display_difficulties()
        diff = input("Difficulty: ")

    return diff
  
  def ask_for_input(self):
    alphabet = string.ascii_lowercase
    inp = input("Guess: ")
    while inp not in alphabet:
            print("{} is not supported in this game. Try again!".format(inp))
            inp = input("Letter: ")

    return inp

  def ask_for_language(self):
    langs = [file for file in os.listdir("./") if file.endswith(".txt")]
    print("\nChoose a language:")
    for l in range(len(langs)):
        print("{}) {:<15}".format(l+1, langs[l]))
    inp = input("\nLanguage: ")
    while inp not in langs:
        print("{} is not supported in this game. Try again!".format(inp))
        inp = input("Try Again. Language: ")

    return inp
  
  def display_dashed_word(self):
    print("-"*30)
    print("Tries left: {}".format(self.tries))

  def right_guess_feedback(self, inp, hidden_word):
    print("\033[1;32mGood job! There is a(n) {}\033[0m\n".format(inp))
    print("\033[1;32mWord: {}\033[0m".format(" ".join(hidden_word)))
  
  def wrong_guess_feedback(self,inp, hidden_word):
    print("\033[1;31mSorry, no letter {}.\033[0m\n".format(inp))
    print("\033[1;31mWord: {}\033[0m".format(" ".join(hidden_word)))

  def game_over_won(self, hidden_word):
    if "_" not in " ".join(hidden_word):
        print("-"*30)
        print("\n\033[1;32;4;5mYOU WON!\033[0m")
        return True
  
  def game_over_lost(self, chosen_word):
    print("-"*30)
    print("\033[1;31;4;5mGAME OVER!\033[0m\n")
    print("The word was '{}'.".format(chosen_word))
