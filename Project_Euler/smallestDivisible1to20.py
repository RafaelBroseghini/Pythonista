"""
    Author: Rafa Broseghini
    Date: 05/29/2018
    Problem: Smallest divisible number from 1 to 20 (individually) without remainder.
"""

import time

def smallest_divisible():
    current = 0
    counts = 0
    oneToTwenty = False
    while not oneToTwenty:
        for n in range(1,21):
            if current != 0:
                if current % n == 0:
                    counts += 1
        """ Break out of the loop. """
        if counts >= 20:
            oneToTwenty = True
            return current
        """ Increase number by 360. I found out I should increment by 360 based on the 1 to 10 division return value."""
        counts = 0
        current += 360
    """ Will never return this runtime errow below. Unless we set a threshold of iterations."""
    return RuntimeError("Not Found!")


def main():
    start = time.time()
    print(smallest_divisible())
    end = time.time()
    print("Took {:.2f}s to perform this action.".format(end-start))

if __name__ == "__main__":
    main()