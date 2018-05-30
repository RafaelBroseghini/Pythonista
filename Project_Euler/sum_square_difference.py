import time

"""
    Author: Rafael Broseghini
    Date: 05/30/2018
    Problem: Find the difference between the sum of the squares of the first one hundred natural
    numbers and the square of the sum.
"""

def sum_of_squares():
    total = 0
    for n in range(1,101):
        total += n**2
    return total

def square_of_sum():
    total = 0
    for n in range(1,101):
        total += n
    return total**2

def difference(a,b):
    return b-a

def main():
    s = time.time()
    diff = difference(sum_of_squares(), square_of_sum())
    print("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: \033[1;32m{}\033[0m".format(diff))
    e = time.time()
    t = e-s
    print("Finished in: {:.5f}".format(t))
if __name__ == '__main__':
    main()