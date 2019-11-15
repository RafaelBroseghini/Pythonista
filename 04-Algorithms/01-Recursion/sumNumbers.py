#!/usr/bin/env python

"""
Calculate the sum of numbers
in a list.
"""


def rec_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + rec_sum(arr[1:])


def main():
    print(rec_sum([1, 2, 3, 4, 5]))
    print(rec_sum([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
