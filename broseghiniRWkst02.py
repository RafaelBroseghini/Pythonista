'''
CS 150 B LAB 2

Purpose: Make calculations using the math and random modules.

Author: Rafael Broseghini.
Date: 03/01/16

Filename: broseghiniRWkst02.py
'''

import math        # Import math module.
print('1. ', round(62.583,2))
print('2. ', round(12345.6789, 3))
print('3. ', 25**4)
print('4. ', math.sqrt(144))
print('5. ', math.pow(25, 3))
print('6. ', math.ceil(62.3))
print('7. ', math.floor(36.9))
print('8. ', math.pi)
print('9a.', math.trunc(145.975))
print('9b.', int(145.975))
print()
print('10.')
import random         # Import the random module.
for i in range(5):    # Run a loop statement to pick 5 random numbers from 0 to 1.00 and print them in different lines.
    print(round(random.random(), 5))
print()
print('11.')
for i in range(10):
    print(random.randint(15, 50), end= ' ') # end = ' ' makes so that all the random picked numbers stay in the same line.
print()
print()
print('12.')
for i in range(10):
    print(random.randrange(15, 51), end = ' ')
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # List.
print()
print()
print('13.')
print(random.choice(numbers))
print()
print('14.')
print(random.sample(numbers, 3))
print()
print('15.')
print('Original list: ', numbers)
random.shuffle(numbers)
print('Shuffled list: ', numbers)


# Done!