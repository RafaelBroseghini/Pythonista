"""
Purpose: Create a program that removes all vowels in a sentence.

Author: Rafael Broseghini
Date: 04/22/2016

Filename: VowelRemoval.py
"""


def removeVowels(sentence):
    vowels = "aeiouAEIOU"

    noVowels = []
    [noVowels.append(ch) for ch in sentence if ch not in vowels]
    return "".join(noVowels)


def main():
    mySentence = input("Enter a sentence: ")
    print("'{}' with no vowels is: '{}'".format(mySentence, removeVowels(mySentence)))


main()
