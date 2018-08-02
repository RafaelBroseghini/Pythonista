#!/usr/bin/env python

"""
Implementation of sequential search on both
ordered and unordered arrays.
"""


def seq_search(arr,elem):
    '''
    Unordered Array
    Time Complexity: O(n)
    '''
    pos = 0
    found = False
    # Will iterate until found or end of array.
    while pos < len(arr) and not found:
        if arr[pos] == elem:
            found = True
        pos += 1
    return found



def seq_search_ordered(arr,elem):
    '''
    Ordered Array
    Time Complexity: O(n)
    ''' 
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not stopped:
        # Will break out of the loop if current elem > parameter passed.
        if arr[pos] > elem:
            stopped = True
        elif arr[pos] == elem:
            found = True
            stopped = True
        pos += 1

    return found


    
    
def main():
    arr = [20,54,1,2,5,78,5,322,23,14]
    print(seq_search(arr,5))
    
    lst = [33,44,56,189,999,1234,55442,888998]
    print(seq_search_ordered(lst,1235))
    
if __name__ == "__main__":
    main()
