#!/usr/bin/env python

"""
Implementation of Binary Search in Python using both
iterative and recursive approach.
"""
from typing import List, Union


def binSearch(arr: List[int], elem: int) -> bool:
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if elem == arr[middle]:
            found = True
        else:
            if arr[middle] < elem:
                first = middle + 1
            elif arr[middle] > elem:
                last = middle - 1
    return found


"""Recursive Binary Search"""


def rec_bin_search(arr: List[int], start: int, end: int, elem: int) -> bool:
    # Base case.
    if start > end:
        return False
    else:
        mid = (start + end) // 2

        if arr[mid] == elem:
            return True
        else:
            if elem > arr[mid]:
                return rec_bin_search(arr, mid + 1, end, elem)
            elif elem < arr[mid]:
                return rec_bin_search(arr, start, mid - 1, elem)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Using Sequential Binary Search: \n")
    print("Looking for elem {} in {}: {}".format(7, arr, binSearch(arr, 7)))
    print("Looking for elem {} in {}: {}".format(13, arr, binSearch(arr, 13)))

    print("\nUsing Recursive Binary Search: \n")
    print(
        "Looking for elem {} in {}: {}".format(
            7, arr, rec_bin_search(arr, 0, len(arr) - 1, 7)
        )
    )
    print(
        "Looking for elem {} in {}: {}".format(
            13, arr, rec_bin_search(arr, 0, len(arr) - 1, 13)
        )
    )


if __name__ == "__main__":
    main()
