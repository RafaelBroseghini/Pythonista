#!/usr/bin/env python

"""
Build a BST from a sorted array.
"""

class BST(object):
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None


def build_tree(array):
    if len(array) == 1:
        return array[0]
    
    mid = len(array)//2

    root = BST(array[mid])
    root.left = build_tree(array[:mid])
    root.right = build_tree(array[mid:])
    return root

def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    root = build_tree(arr)

    print(root.data)
    print(root.left.data)
    print(root.right.data)

if __name__ == '__main__':
    main()