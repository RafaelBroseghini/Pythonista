"""
    Author: Rafael Broseghini
    Date: 05/29/2018
    Problem: Return sum of even fibonacci numbers that do not exceed 4M.
"""

def fib_iterative():
    prev = 1
    current = 2
    sum_even_fibonacci = 2
    four_million = 4000000

    while current < four_million:
        next_ = prev + current
        if next_ % 2 == 0:
            sum_even_fibonacci += next_
        prev = current
        current = next_

    return "\n\033[1;31mSum offibonacci numbers less than 4M:\033[0m \033[1;32m{}\033[0m\n".format(sum_even_fibonacci)

def main():
    print(fib_iterative())

if __name__ == "__main__":
    main()
