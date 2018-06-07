import re
import random
import string

class Hangman():
    def __init__(self, words=[], used_letters = [], tries=10):
        self.words = words
        self.tries = tries
        self.used_letters = used_letters

        with open("english.txt","r") as file:
            pattern = re.compile(r"\n")
            lst = file.readlines()
            for word in range(len(lst)):
                lst[word] = re.sub(pattern,"",lst[word])
                if len(lst[word]) >= 3 and len(lst[word]) <= 5:
                    self.words.append(lst[word]) 
    

    def choose_word(self):
        word = random.choice(self.words)
        self.words.remove(word)
        return word

    def dashed_word(self,word):
        sub = re.sub(r".","_",word)
        return list(sub)

    def ask_for_input(self):
        alphabet = string.ascii_lowercase
        inp = input("Guess: ")
        while True:
            if inp not in alphabet:
                print("{} is not supported in this game. Try again!".format(inp))
                inp = input("Letter: ")
            else:
                return inp
    
    def letter_has_been_used(self, letter):
        for i in range(len(self.used_letters)):
            if self.used_letters[i] == letter:
                return True
        return False


    
    def right_guess(self, word, dashed_word, letter):
        i = 0
        in_word = False
        while i < len(word):
            if word[i] == letter:
                dashed_word[i] = letter
                in_word = True
            i += 1
        if in_word:
            return True
    
    def success(self, inp, puzzle_word):
        print("\033[1;32mGood job! There is a(n) {}\033[0m\n".format(inp))
        print("\033[1;32mWord: {}\033[0m".format(" ".join(puzzle_word)))
    
    def failure(self,inp, puzzle_word):
        print("\033[1;31mSorry, no letter {}.\033[0m\n".format(inp))
        print("\033[1;31mWord: {}\033[0m".format(" ".join(puzzle_word)))

    def won(self, dashed_word):
        if "_" not in " ".join(dashed_word):
            return True

    def play_game(self):
        chosen_word = self.choose_word()
        puzzle_word = self.dashed_word(chosen_word)
        won = False
        print("The word is: {}\n".format(" ".join(puzzle_word)))
        while self.tries > 0 and not won:
            print("-"*30)
            print("Try: {}".format(11-self.tries))
            inp = self.ask_for_input()
            while self.letter_has_been_used(inp):
                print("You already used letter: '{}'".format(inp))
                inp = self.ask_for_input()
            self.used_letters.append(inp)
            print("Used letters: {}\n".format(sorted(self.used_letters)))
            if self.right_guess(chosen_word,puzzle_word,inp):
                self.success(inp,puzzle_word)
            else:
                self.failure(inp, puzzle_word)
            

            if self.won(puzzle_word):
                print("Wooo! You figured out the word '{}' in {} tries.".format(chosen_word, 11-self.tries))
                won = True
            else:
                self.tries -= 1

        if self.tries == 0:
            print("The word was '{}'.".format(chosen_word))

