'''
Purpose: Create a number guessing game.

Author: Rafael Broseghini
Date: 04/09/2016

Filename: GuessNumber.py
'''

import random
print('***** NUMBER GUESSING GAME *****')
def main():
            randomNumber = random.randint(1, 50)
            myChoice = int(input('Guess a number between 1 and 50: '))
            guesses = 1
            while myChoice != randomNumber:
                        guesses += 1
                        if myChoice < randomNumber:
                                    myChoice = int(input('Too low - Try again: '))
                        elif myChoice > randomNumber:
                                    myChoice = int(input('Too high - Try again: '))
            if guesses != 1:
                        print('You got it in {} tries'.format(guesses))
            else:
                        print('You got it in 1 try.')
main()
