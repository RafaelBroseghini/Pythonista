#!/usr/bin/env python3

"""
Python implementation of Morse code encoder
and decoder.
"""

__author__ = "Rafael Broseghini"


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def height(self):
        if self.key is None:
            return 0
        return (
            max(
                self.leftChild.height() if self.leftChild is not None else 0,
                self.rightChild.height() if self.rightChild is not None else 0,
            )
            + 1
        )

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        return str(self.key)


def build_tree():
    morse_tree = BinaryTree("")
    with open("morse.txt") as file:
        morse_dict = dict()
        for line in file:
            (key, val) = line.split()
            morse_dict[key] = val
            cur_node = morse_tree
            for dash_or_dot in val:
                if dash_or_dot == ".":
                    if cur_node.getLeftChild() is None:
                        cur_node.insertLeft("")
                    cur_node = cur_node.getLeftChild()
                else:
                    if cur_node.getRightChild() is None:
                        cur_node.insertRight("")
                    cur_node = cur_node.getRightChild()
            cur_node.setRootVal(key)
        return morse_tree


def decode(message: str, tree: BinaryTree) -> list:
    message = message.split(" ")
    decoder = []
    for part in message:
        cur_node = tree
        for symbol in part:
            if symbol == ".":
                cur_node = cur_node.getLeftChild()
            else:
                cur_node = cur_node.getRightChild()
        decoder.append(str(cur_node))
    result = ",".join(decoder).replace(",", "")
    return result


def encode(message: str, tree: BinaryTree) -> str:
    output = ""
    message = message.lower().split(" ")
    for word in message:
        for letter in word:
            output = output + findpath(tree, letter, "") + " "
    return output


def findpath(mytree: BinaryTree, letter: str, path: str) -> str:
    if not mytree:
        return False
    elif mytree.getRootVal() == letter:
        return path
    else:
        return findpath(mytree.getLeftChild(), letter, path + ".") or findpath(
            mytree.getRightChild(), letter, path + "-"
        )


def main():
    morse_code_tree = build_tree()
    print(
        "The right child of the root of the MorseTree is:",
        morse_code_tree.getRightChild(),
    )
    print(
        "The left child of the root of the MorseTree is:",
        morse_code_tree.getLeftChild(),
    )
    print(
        "The right child of",
        morse_code_tree.getRightChild(),
        "is:",
        morse_code_tree.getRightChild().getRightChild(),
    )
    print(
        "The left child of",
        morse_code_tree.getLeftChild(),
        "is:",
        morse_code_tree.getLeftChild().getLeftChild(),
    )
    print("The height of the entire MorseTree is:", morse_code_tree.height())
    print(
        "My message in morse code to you is:",
        decode(
            "--. .. ...- . ..--.- -- . ..--.- .- -. ..--.- .- ..--\
    .- ..-. --- .-. ..--.- - .... .. ... ..--.- -.-. .-.. .- ... ...",
            morse_code_tree,
        ),
    )
    print(
        'Translating "Simple is better than complex" to morse code:',
        encode("Simple is better than complex", morse_code_tree),
    )


if __name__ == "__main__":
    main()
