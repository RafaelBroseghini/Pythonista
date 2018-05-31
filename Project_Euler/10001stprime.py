import time

"""
    Author: Rafael Broseghini
    Date: 05/30/2018
    Problem: Find the largest number palindrome from the product of 3 digits.
"""

def is_prime(n):
    prime = False
    i = 2
    while not prime and i < n:
        if n % i == 0:
            prime = True
        i += 1
    return not prime
        
def find_prime_seq(b):
    count = 0
    i = 2
    while count < b:
        if is_prime(i):
            count += 1
            print(count)
        i += 1
    return i - 1


def main():
    s = time.time()
    print(find_prime_seq(10001))
    e = time.time()
    t = e-s
    print("Finished in: {:.5f}s".format(t))

if __name__ == '__main__':
    main()