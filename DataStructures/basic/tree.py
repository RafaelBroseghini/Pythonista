class BinaryTree(object):
    def __init__(self,root):
        self.root       = root
        self.leftChild  = None
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
    
    # print(tree.root)
    
    leftH = maxHeight(tree.leftChild)
    rightH = maxHeight(tree.rightChild)

    return max(leftH, rightH) + 1

def main():
    b = BinaryTree(10)
    b.insertLeft(9)
    a = b.getLeftChild()
    for i in range(100):
        a.insertRight(i)
            # for i in range(10):
    #     b.insertLeft(i)
    #     b.insertRight(i+10)

    print(maxHeight(b))
if __name__ == '__main__':
    main()