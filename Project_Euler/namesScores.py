import time
import re

"""
    Author: Rafael Broseghini
    Date: 05/31/2018

    Problem: Begin by sorting it into alphabetical order. 
    Then working out the alphabetical value for each name, 
    multiply this value by its alphabetical position in the list to obtain a name score.
    For example, when the list is sorted into alphabetical order, COLIN, 
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
    So, COLIN would obtain a score of 938 × 53 = 49714.
    What is the total of all the name scores in the file?
"""

ALPHABET = " abcdefghijklmnopqrstuvwxyz"

def read_from_file_sorted_list():
    with open("names.txt") as file:
        for line in file:
            lst = re.sub('"',"",line).split(",")
    return sorted(lst)

def word_score(word):
    score = 0
    for c in range(len(word)):
        score += ALPHABET.index(word[c])
    return score

def list_word_score(lst):
    for word in range(len(lst)):
        lst[word] = word_score(lst[word].lower()) * (word+1)
    return sum(lst)

def main():
    s = time.time()
    #function goes here!
    lst = read_from_file_sorted_list()
    score_total = list_word_score(lst)
    print("The sum of all name scores in names.txt is: \033[1;32m{}\033[0m".format(score_total))
    e = time.time()
    t = e-s
    print("-"*53)
    print("Finished in: {:.5f}s".format(t))

if __name__ == '__main__':
    main()

