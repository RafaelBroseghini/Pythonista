class BinarySearchTree(object):

    """
        No deletion method on this one.
        For purposes of study.
    """

    def __init__(self, data):
        self.root       = data
        self.leftChild  = None
        self.rightChild = None

    def getRootVal(self):
        return self.root
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def insertNode(self, node):
        if node > self.getRootVal():
            if self.getRightChild() is None:
                self.rightChild = BinarySearchTree(node)
            else:
                self.rightChild.insertNode(node)
        else:
            if self.getLeftChild() is None:
                self.leftChild = BinarySearchTree(node)
            else: 
                self.leftChild.insertNode(node)
    
    def searchNode(self, value):
        if value < self.getRootVal() and self.getLeftChild():
            return self.leftChild.searchNode(value)
        if value > self.getRootVal() and self.getRightChild():
            return self.rightChild.searchNode(value)
        
        return value == self.getRootVal()
            


def main():
    b = BinarySearchTree(1)
    b.insertNode(10)
    for i in range(3,90):
        b.insertNode(i)
        b.insertNode(i+100)
        b.insertNode(i-50)

    print(b.searchNode(-47))

if __name__ == '__main__':
    main()