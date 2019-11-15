#!/usr/bin/env python

"""
Implementation of a Stack
using a Linked List.

Pushing and popping are done
in constant time O(1) and we
do not need to worry about the
amortized case of a Python list
resizing.
"""


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, new_element):
        self.head = Node(new_element, self.head)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Linked Stack is already empty.")

        res = self.head
        self.head = res.next
        self.size -= 1
        return res

    def peek(self):
        if self.isEmpty():
            raise Exception("Linked Stack is already empty.")
        return self.head.data

    def isEmpty(self):
        return self.size == 0


def main():
    ls = LinkedStack()

    ls.push(3)
    ls.push(2)
    ls.push(1)
    print("popping head", ls.pop().data)
    print("popping head", ls.pop().data)
    print("popping head", ls.pop().data)
    # print("popping head", ls.pop().data)

    print("head", ls.peek())
    print("size", len(ls))


if __name__ == "__main__":
    main()
