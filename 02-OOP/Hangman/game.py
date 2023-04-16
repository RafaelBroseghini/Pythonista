import random
import string
import re

from announcer import Announcer


class Hangman:
    def __init__(self, words=None, used_letters=None, tries=10):
        if words is None:
            words = []
        if used_letters is None:
            used_letters = []
        self.words = words
        self.tries = tries
        self.used_letters = used_letters

    def read_from_file(self, b, t, lang):
        with open(f"./langs/{lang}", "r") as file:
            lines = file.read().splitlines()
            self.words = [word.lower() for word in lines if b <= len(word) <= t]

    def ask_for_input(self):
        alphabet = string.ascii_lowercase
        inp = input("Guess: ")
        while inp not in alphabet:
            print(f"{inp} is not supported in this game. Try again!")
            inp = input("Letter: ")
        return inp

    def choose_word(self):
        word = random.choice(self.words)
        self.words.remove(word)
        return word

    def hidden_word(self, word):
        return ["_" for _ in word]

    def letter_has_been_used(self, letter):
        return letter in self.used_letters

    def right_guess(self, word, hidden_word, letter):
        in_word = False
        for i, char in enumerate(word):
            if char == letter:
                hidden_word[i] = letter
                in_word = True
        return in_word

    def play_game(self):
        announcer = Announcer()
        diff = announcer.display_supported_difficulties()
        lang = announcer.ask_for_language()

        if not lang.endswith(".txt"):
            lang += ".txt"

        self.read_from_file(
            announcer.difficulty[diff][1][0], announcer.difficulty[diff][1][1], lang
        )

        chosen_word = self.choose_word()
        hidden_word = self.hidden_word(chosen_word)
        won = False
        print(f"The word is: {' '.join(hidden_word)}\n")

        while self.tries > 0 and not won:
            announcer.display_dashed_word()
            inp = announcer.ask_for_input()
            while self.letter_has_been_used(inp):
                print(f"You already used letter: '{inp}'")
                inp = self.ask_for_input()
            self.used_letters.append(inp)
            print(f"Used letters: {sorted(self.used_letters)}\n")

            if self.right_guess(chosen_word, hidden_word, inp):
                announcer.right_guess_feedback(inp, hidden_word)
            else:
                announcer.wrong_guess_feedback(inp, hidden_word)
                announcer.tries -= 1

            if announcer.game_over_won(hidden_word):
                won = True
            elif announcer.tries == 0:
                announcer.game_over_lost(chosen_word)
                exit()
