# Implementation of a recursive Binary Search.

"""
Compute middle, if greater, do binary search on right side,
else, do binary search on left side.
"""


def binary_search(arr, target, start, end):
    # Base case.
    if start > end:
        return False

    mid = (end + start) // 2

    if arr[mid] == target:
        return True
    elif target > arr[mid]:
        start = mid + 1
        # Recursive call moving towards the base case.
        return binary_search(arr, target, start, end)
    else:
        end = mid - 1
        # Recursive call moving towards the base case.
        return binary_search(arr, target, start, end)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print("\nThis is the array: ", arr, "\n")
    print("Is item 1 in arr? ", binary_search(arr, 1, 0, len(arr) - 1))
    print("Is item 2 in arr? ", binary_search(arr, 2, 0, len(arr) - 1))
    print("Is item 12 in arr? ", binary_search(arr, 12, 0, len(arr) - 1))
    print("Is item 13 in arr? ", binary_search(arr, 13, 0, len(arr) - 1))
    print("Is item 15 in arr? ", binary_search(arr, 15, 0, len(arr) - 1))
    print("Is item 19 in arr? ", binary_search(arr, 19, 0, len(arr) - 1))
    print("Is item 21 in arr? ", binary_search(arr, 21, 0, len(arr) - 1))


if __name__ == "__main__":
    main()
