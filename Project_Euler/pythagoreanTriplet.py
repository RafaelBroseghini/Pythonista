import time
import math
"""
    Author: Rafael Broseghini
    Date: 05/30/2018
    Problem: There exists exactly one Pythagorean triplet for which a + b + c = 1000.

    a < b < c
"""

def pythagorean_triplet():
    for i in range(1,999):
        for j in range(1,999):
            k = i**2 + j**2
            if i + j + math.sqrt(k) == 1000.0:
                return i*j*round(math.sqrt(k))
        

def main():
    s = time.time()
    print("Product (a*b*c) of a + b + c = 1000 Pythagorean triplet: \033[1;32m{}\033[0m".format(pythagorean_triplet()))
    e = time.time()
    t = e-s
    print("Finished in: {:.5f}s".format(t))
if __name__ == '__main__':
    main()