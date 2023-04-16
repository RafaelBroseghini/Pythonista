import os
import string

class Announcer:
    def __init__(self, difficulty=None, tries=10):
        if difficulty is None:
            difficulty = {
                "e": ["easy", (3, 4)],
                "i": ["intermediate", (5, 7)],
                "h": ["hard", (8, 12)],
            }
        self.difficulty = difficulty
        self.tries = tries

    def display_difficulties(self):
        for k, v in self.difficulty.items():
            print(f"({k}): {v[0]}")

    def display_supported_difficulties(self):
        print("Hi there! Let's play hangman!")
        print("-" * 30 + "\n")
        print("First you need to select a difficulty: \n")
        self.display_difficulties()
        diff = input("Difficulty: ")
        while diff not in self.difficulty:
            print(f"{diff} is not a(n) supported difficulty input. Try again!\n")
            self.display_difficulties()
            diff = input("Difficulty: ")
        return diff

    def ask_for_input(self):
        alphabet = string.ascii_lowercase
        inp = input("Guess: ")
        while inp not in alphabet:
            print(f"{inp} is not supported in this game. Try again!")
            inp = input("Letter: ")
        return inp

    def ask_for_language(self):
        langs = [file for file in os.listdir("./") if file.endswith(".txt")]
        print("\nChoose a language:")
        for idx, lang in enumerate(langs, start=1):
            print(f"{idx}) {lang:<15}")
        inp = input("\nLanguage: ")
        while inp not in langs:
            print(f"{inp} is not supported in this game. Try again!")
            inp = input("Try Again. Language: ")
        return inp

    def display_dashed_word(self):
        print("-" * 30)
        print(f"Tries left: {self.tries}")

    def right_guess_feedback(self, inp, hidden_word):
        print(f"\033[1;32mGood job! There is a(n) {inp}\033[0m\n")
        print(f"\033[1;32mWord: {' '.join(hidden_word)}\033[0m")

    def wrong_guess_feedback(self, inp, hidden_word):
        print(f"\033[1;31mSorry, no letter {inp}.\033[0m\n")
        print(f"\033[1;31mWord: {' '.join(hidden_word)}\033[0m")

    def game_over_won(self, hidden_word):
        if "_" not in " ".join(hidden_word):
            print("-" * 30)
            print("\n\033[1;32;4;5mYOU WON!\033[0m")
            return True

    def game_over_lost(self, chosen_word):
        print("-" * 30)
        print("\033[1;31;4;5mGAME OVER!\033[0m\n")
        print(f"The word was '{chosen_word}'.")

