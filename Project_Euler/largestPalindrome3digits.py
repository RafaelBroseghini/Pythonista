import time

"""
    Author: Rafael Broseghini
    Date: 05/30/2018
    Problem: Find the largest number palindrome from the product of 3 digits.
"""
def largest_palindrome_3digit_product():
    largest_palindrome = 101
    for n in range(100,1000):
        for i in range(100, 1000):
            p = str(n*i)
            if p == p[::-1] and n*i > largest_palindrome:
                largest_palindrome = n*i

    return largest_palindrome

def main():
    s = time.time()
    print("Largest palindrome from a product of two three digit numbers is: {}".format(test_On2()))
    e = time.time()
    t = e-s
    print("Finished in: {:.5f}".format(t))

if __name__ == '__main__':
    main()