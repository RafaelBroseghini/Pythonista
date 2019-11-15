#!/usr/bin/env python

"""
Implementation of the Word Ladder Algorithm
using two stacks.
"""

# Creating sets for words of 3, 4 and 5 letters from words.txt
LETTER_WORDS_3 = set()
LETTER_WORDS_4 = set()
LETTER_WORDS_5 = set()


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return (str("\n".join(self.items))).upper()

    def copy(self):
        stack_clone = Stack()
        stack_clone.items = self.items[:]
        return stack_clone


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# adding words based on length to respective sets.
def readfile(filename):
    with open(filename, "r") as file:
        for line in file:
            word = line.strip()
            if len(word) == 3:
                LETTER_WORDS_3.add(word)
            if len(word) == 4:
                LETTER_WORDS_4.add(word)
            if len(word) == 5:
                LETTER_WORDS_5.add(word)
        print("There are", len(LETTER_WORDS_3), "three letter words.")
        print("There are", len(LETTER_WORDS_4), "four letter words.")
        print("There are", len(LETTER_WORDS_5), "five letter words.")


# Function identifies words that are different by only one letter.
def diff_by_one_letter(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for x in range(len(word1)):
            if word1[x] != word2[x]:
                count += 1
        if count == 1:
            return word2


# Function identifies words that are different by only one letter from all words and used words.
def diff_by_one_letter_all(word, all_words, used_words):
    result = [
        x for x in all_words if diff_by_one_letter(x, word) and x not in used_words
    ]
    return result


def main():
    readfile("words.txt")
    words_to_use = None
    print("Let's try to find a word ladder from starting word until end word!")
    word_start = input("Enter starting word: ").lower()
    word_end = input("Enter ending word: ").lower()
    if (
        len(word_start) > 5
        or len(word_start) < 3
        or len(word_end) > 5
        or len(word_end) < 3
    ):
        raise Exception("Both of your input words must be a 3, 4 or 5 letter word.")
    if len(word_start) != len(word_end):
        raise Exception("Starting word and ending word must be of the same length.")
    if len(word_start) == 3:
        words_to_use = LETTER_WORDS_3
    if len(word_start) == 4:
        words_to_use = LETTER_WORDS_4
    if len(word_start) == 5:
        words_to_use = LETTER_WORDS_5
    print("Let's turn", word_start, "into", word_end + ".")
    words_used = set(word_start)
    ladder_Start = Stack()
    ladder_Start.push(word_start)
    all_ladders = Queue()
    all_ladders.enqueue(ladder_Start)
    result_ladder = Stack()

    # While loop keeps enqueueing and dequeueing stacks from current ladder until candidate word == end word.
    found = False
    while not all_ladders.isEmpty() and not found:
        current_ladder = all_ladders.dequeue()
        possible_words = diff_by_one_letter_all(
            current_ladder.peek(), words_to_use, words_used
        )
        for candidate_word in possible_words:
            new_ladder = current_ladder.copy()
            new_ladder.push(candidate_word)
            words_used.add(candidate_word)
            if candidate_word == word_end:
                print("Ladder found:")
                result_ladder = new_ladder.copy()
                found = True
            else:
                all_ladders.enqueue(new_ladder)
    if result_ladder.size() == 0:
        print(
            "It is not possible to turn",
            word_start,
            "into",
            word_end,
            "based on the words present in the .txt document provided.",
        )
    print(result_ladder)


main()
