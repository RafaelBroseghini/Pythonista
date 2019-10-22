#!/usr/bin/env python

"""
Find the minimun element in a 
Python List using recursion.
"""

def min_element(arr, last):
    if len(arr) == 1:
        return last
    else:
        if arr[0] < last:
            new_min = arr[0]
        else:
            new_min = last
        
    return min_element(arr[1:],new_min)


print(min_element([-20,2,3,4,5,6,-1,66],66))