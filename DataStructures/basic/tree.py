class BinaryTree(object):
    """docstring for BinaryTree."""
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newBranch):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newBranch)
        else:
            temp = BinaryTree(newBranch)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, newBranch):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newBranch)
        else:
            temp = BinaryTree(newBranch)
            temp.rightChild = self.rightChild
            self.rightChild = temp

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, nv):
        self.key = nv

    def getRootVal(self):
        return self.key

t = BinaryTree(5)
t.insertLeft(9)
t.insertLeft(10)

print(t.getLeftChild())
