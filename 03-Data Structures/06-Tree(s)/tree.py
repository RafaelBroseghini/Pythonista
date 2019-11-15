from queue import Queue


class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def getRootVal(self):
        return self.root

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def insertLeft(self, value):
        if self.getLeftChild() is None:
            self.leftChild = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, value):
        if self.getRightChild() is None:
            self.rightChild = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.rightChild = self.rightChild
            self.rightChild = temp


def maxHeight(tree):
    if tree is None:
        return 0

    leftH = maxHeight(tree.leftChild)
    rightH = maxHeight(tree.rightChild)

    return max(leftH, rightH) + 1


def BFS(tree):
    visited = set()
    q = Queue()
    q.enqueue(tree)
    while not q.isEmpty():
        current = q.dequeue()
        print(current.getRootVal())
        if current not in visited:
            visited.add(current)
            if current.getLeftChild() is not None:
                q.enqueue(current.getLeftChild())
            if current.getRightChild() is not None:
                q.enqueue(current.getRightChild())
    return visited


def main():
    b = BinaryTree(1)
    b.insertLeft(2)
    b.insertRight(3)
    a = b.getLeftChild()
    a.insertLeft(4)
    a.insertRight(5)
    c = b.getRightChild()
    c.insertLeft(6)
    c.insertRight(7)
    d = a.getLeftChild()
    d.insertLeft(8)
    d.insertRight(9)

    print("Breadth first search on the tree: ")
    BFS(b)

    print("\nHeight of tree: \033[1;33m{}\033[0m\n".format(maxHeight(b)))


if __name__ == "__main__":
    main()
