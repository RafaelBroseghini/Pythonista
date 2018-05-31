import time

"""
    Author: Rafael Broseghini
    Date: 05/30/2018
    Problem: What is the largest prime factor of the number 600851475143 ?
"""
def is_prime(n):
    prime = False
    i = 2
    while not prime and i < n:
        if n % i == 0:
            prime = True
        i += 1
    return not prime

def find_prime_factor(n):
    found = False
    i = n
    while not found:
        print(i)
        if is_prime(i) and n % i == 0:
            found = True
            largest_factor = i
        if  n % 2 != 0:
            i -= 2
        else:
            i -= 1
    return largest_factor

def main():
    s = time.time()
    print(largest_prime_factor(600851475143))
    e = time.time()
    t = e-s
    print("Finished in: {:.5f}s".format(t))

if __name__ == '__main__':
    main()