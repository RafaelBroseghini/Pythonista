import re
import random
import string

class Hangman():
    def __init__(self, words=[], used_letters = [], tries=10, difficulty={"e":["easy",(3,4)],"i":["intermediate",(5,7)],"h":["hard",(8,12)]}):
        self.words = words
        self.tries = tries
        self.used_letters = used_letters
        self.difficulty = difficulty

    def display_difficulties(self):
        for k,v in self.difficulty.items():
            print("({}): {}".format(k,v[0]))

    def display_intro_set_difficulty(self):
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

    def read_from_file(self,b,t):
        with open("english.txt","r") as file:
            pattern = re.compile(r"\n")
            lst = file.readlines()
            for word in range(len(lst)):
                lst[word] = re.sub(pattern,"",lst[word])
                if len(lst[word]) >= b and len(lst[word]) <= t:
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
        while inp not in alphabet:
                print("{} is not supported in this game. Try again!".format(inp))
                inp = input("Letter: ")

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
    
    def right_guess_feedback(self, inp, puzzle_word):
        print("\033[1;32mGood job! There is a(n) {}\033[0m\n".format(inp))
        print("\033[1;32mWord: {}\033[0m".format(" ".join(puzzle_word)))
    
    def wrong_guess_feedback(self,inp, puzzle_word):
        print("\033[1;31mSorry, no letter {}.\033[0m\n".format(inp))
        print("\033[1;31mWord: {}\033[0m".format(" ".join(puzzle_word)))

    def game_over_won(self, chosen_word, dashed_word, tries):
        if "_" not in " ".join(dashed_word):
            print("-"*30)
            print("\n\033[1;32;4;5mYOU WON!\033[0m")
            print("Wooo! You figured out the word '{}' in {} tries.".format(chosen_word, 11-self.tries))
            return True
    
    def game_over_lost(self, chosen_word):
        print("-"*30)
        print("\033[1;31;4;5mGAME OVER!\033[0m\n")
        print("The word was '{}'.".format(chosen_word))

    def play_game(self):
        diff = self.display_intro_set_difficulty()
        self.read_from_file(self.difficulty[diff][1][0],self.difficulty[diff][1][1])
        chosen_word = self.choose_word()
        puzzle_word = self.dashed_word(chosen_word)
        won = False
        print("The word is: {}\n".format(" ".join(puzzle_word)))
        while self.tries > 0 and not won:
            print("-"*30)
            print("Tries left: {}".format(self.tries))
            inp = self.ask_for_input()
            while self.letter_has_been_used(inp):
                print("You already used letter: '{}'".format(inp))
                inp = self.ask_for_input()
            self.used_letters.append(inp)
            print("Used letters: {}\n".format(sorted(self.used_letters)))
            if self.right_guess(chosen_word,puzzle_word,inp):
                self.right_guess_feedback(inp,puzzle_word)
            else:
                self.wrong_guess_feedback(inp, puzzle_word)
                self.tries -= 1
            

            if self.game_over_won(chosen_word, puzzle_word, self.tries):
                won = True
            elif self.tries == 0:
                self.game_over_lost(chosen_word)

