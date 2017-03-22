'''
Purpose: Create a program that fills a list with random numbers, sorts it, squares and cubes the numbers.

Author: Rafael Broseghini
Date: 04/22/2016

Filename: broseghiniWk08P2.py
'''
# This imports the random module.
import random

# This creates the originalList function.
def originalList():
    
    # This creates an empty list and assigns it to the variable myOriginalList.
    myOriginalList = []           
    
    # This creates a for loop that chooses 10 different random numbers, appends them to myOriginalList, prints them, and prints them in sorted order.
    for i in range(10):
        randomNumbers = random.randint(1, 10)
        myOriginalList.append(randomNumbers)
    print('Original List: ', myOriginalList)
    print('Sorted List: ', sorted(myOriginalList))
    print()
    
    # This uses list comprehension to square each number.
    squaredList = [number **2 for number in myOriginalList if number % 2 == 0]
    
    # This uses list comprehension to cube each number.
    cubedList = [number ** 3 for number in myOriginalList if number % 2 != 0]
    
    # This prints the list with all numbers squared and in sorted order.
    print('Square of evens: ', sorted(squaredList))
    
    # This prints the list with all numbers cubed and in sorted order.
    print('Cube of odds: ', sorted(cubedList))

originalList()
