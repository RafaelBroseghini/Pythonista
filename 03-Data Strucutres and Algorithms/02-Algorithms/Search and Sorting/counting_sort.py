"""
Implementation of the counting sort algorithm.

This algorithm only sorts integer based arrays.

Time complexity: O(n+m)
Space complexity: O(n+m)

"""


def count_sort(array: list) -> list:
    bit_array = [0 for i in range(max(array)+1)]

    for num in array:
        bit_array[num] = 1

    return [n for n in range(len(bit_array)) if bit_array[n] == 1]


def main():
    a = [99,4,3,78,5,25,67,12,62,5,8,44,72,5,0]

    print(count_sort(a))

if __name__ == "__main__":
    main()