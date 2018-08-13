#!/usr/bin/env python

"""
Calculate the consecutive sum of 
each digit passed in as parameter.
"""

def consecutive_sum(number):
    if number // 10 < 1:
        return number
    return number % 10 + consecutive_sum(number // 10)


def main():
    assert consecutive_sum(123456789) == 45
    assert consecutive_sum(12) == 3
    assert consecutive_sum(999999999) == 81

    print("Passed all tests!")

if __name__ == '__main__':
    main()