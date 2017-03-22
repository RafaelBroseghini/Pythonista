'''
Purpose: Create a program that removes all vowels in a sentence.

Author: Rafael Broseghini
Date: 04/22/2016

Filename: RemoveVowels.py
'''
# This creates a main function.
def main():
    #This gets the user input and assigns it to the variable mySentence.
    mySentence = input('Enter a sentence: ')
   
    # This calls the removeVowels function, assigns mySentence as a parameter of that function and prints the user input with no vowels.
    print(removeVowels(mySentence))

# This creates a removeVowels function.
def removeVowels(sentence):
    vowels = 'aeiouAEIOU'
    
    # This creates an empty list.
    noVowels = [ ]
    
    # This identifies the non vowels in the user input sentence and adds it to a list.
    [noVowels.append(ch) for ch in sentence if ch not in vowels]
    
    # This joins the list into a string statement.
    return ''.join(noVowels)

# This calls and executes main function.
main()


