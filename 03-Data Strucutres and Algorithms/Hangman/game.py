import random
import string
import re

from announcer import Announcer


class Hangman(object):
    def __init__(self, words=[], used_letters=[], tries=10):
        self.words = words
        self.tries = tries
        self.used_letters = used_letters

    def read_from_file(self, b, t):
        with open("pt-br.txt", "r") as file:
            pattern = re.compile(r"\n")
            lst = file.readlines()
            for word in range(len(lst)):
                lst[word] = re.sub(pattern, "", lst[word])
                if len(lst[word]) >= b and len(lst[word]) <= t:
                    self.words.append(lst[word])

    def ask_for_input(self):
        """Ask user for input. Validate it."""
        alphabet = string.ascii_lowercase
        inp = input("Guess: ")
        while inp not in alphabet:
            print("{} is not supported in this game. Try again!".format(inp))
            inp = input("Letter: ")

        return inp

    def choose_word(self):
        """Choose random word from file."""
        word = random.choice(self.words)
        self.words.remove(word)
        return word

    def hidden_word(self, word):
        """Substitute all letters for _."""
        sub = re.sub(r".", "_", word)
        return list(sub)

    def letter_has_been_used(self, letter):
        """Check if letter has already been used."""
        for i in range(len(self.used_letters)):
            if self.used_letters[i] == letter:
                return True
        return False

    def right_guess(self, word, hidden_word, letter):
        """Check if guess is in word."""
        i = 0
        in_word = False
        while i < len(word):
            if word[i] == letter:
                hidden_word[i] = letter
                in_word = True
            i += 1
        if in_word:
            return True

    def play_game(self):
        """Playing the game."""
        announcer = Announcer()
        diff = announcer.display_supported_difficulties()
        self.read_from_file(announcer.difficulty[diff][1][0],
                            announcer.difficulty[diff][1][1])
        chosen_word = self.choose_word()
        hidden_word = self.hidden_word(chosen_word)
        won = False
        print("The word is: {}\n".format(" ".join(hidden_word)))

        while self.tries > 0 and not won:
            announcer.display_dashed_word()
            inp = announcer.ask_for_input()
            while self.letter_has_been_used(inp):
                print("You already used letter: '{}'".format(inp))
                inp = self.ask_for_input()
            self.used_letters.append(inp)
            print("Used letters: {}\n".format(sorted(self.used_letters)))

            if self.right_guess(chosen_word, hidden_word, inp):
                announcer.right_guess_feedback(inp, hidden_word)
            else:
                announcer.wrong_guess_feedback(inp, hidden_word)
                announcer.tries -= 1

            # Check if game has been won or not.
            if announcer.game_over_won(hidden_word):
                won = True
            elif announcer.tries == 0:
                announcer.game_over_lost(chosen_word)
