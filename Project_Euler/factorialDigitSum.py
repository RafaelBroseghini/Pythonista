import time
import re

"""
    Author: Rafael Broseghini
    Date: 05/30/2018
    Problem: Find the sum of the digits in the number 100!
"""

def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n-1)

def sum_of_digits(n):
    lst = re.sub("",",",str(n)).split(",")
    lst = [int(x) for x in lst if x != ""]
    return sum(lst)

def main():
    s = time.time()
    n = factorial_rec(100)
    print(sum_of_digits(n))
    e = time.time()
    t = e-s
    print("Finished in: {:.5f}s".format(t))

if __name__ == '__main__':
    main()