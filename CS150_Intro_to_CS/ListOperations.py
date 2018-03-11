'''
Purpose: Create a program that fills a list with random numbers, sorts it, squares and cubes the numbers.

Author: Rafael Broseghini
Date: 04/22/2016

Filename: CubingAndSquaringNumbersFromAList.py
'''
import random

def originalList():

    myOriginalList = []

    for i in range(10):
        randomNumbers = random.randint(1, 50)
        myOriginalList.append(randomNumbers)
    print('Original List: ', myOriginalList)
    print('Sorted List: ', sorted(myOriginalList))
    print()
    squaredList = [number **2 for number in myOriginalList if number % 2 == 0]
    cubedList = [number ** 3 for number in myOriginalList if number % 2 != 0]
    print('Square of evens: ', sorted(squaredList))
    print('Cube of odds: ', sorted(cubedList))

originalList()
