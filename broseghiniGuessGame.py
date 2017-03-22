'''
Purpose: Create a number guessing game.

Author: Rafael Broseghini
Date: 04/09/2016

Filename: broseghiniGuessGame.py
'''

import random # Imports random module.
print('***** NUMBER GUESSING GAME *****')
def main(): # This function takes the user input, double checks if it matches the random picked number and keeps tracks of the number of tries until the number gets correctly guessed while giving tips if it's too high or too low.
            randomNumber = random.randint(1, 50) # This picks a number from one to 50, inclusive.
            myChoice = int(input('Guess a number between 1 and 50: ')) # User input.
            guesses = 1        # This initializes a variable.
            while myChoice != randomNumber:
                        guesses += 1 # Each time you entry an input it adds 1 to the variable guesses.
                        if myChoice < randomNumber:
                                    myChoice = int(input('Too low - Try again: ')) # If user input is less than random.randint, program prints this.
                        elif myChoice > randomNumber:
                                    myChoice = int(input('Too high - Try again: ')) # If user input is greater than random.randint program prints this.
            if guesses != 1:
                        print('You got it in {} tries'.format(guesses))
            else:
                        print('You got it in 1 try.')    # If you guess correctly in the first try, prints this.
main()
    
