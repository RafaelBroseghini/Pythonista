from tree import BinaryTree

def inorderTraversal(tree):
    if tree != None:
        inorderTraversal(tree.getLeftChild())
        print(tree.getRootVal())
        inorderTraversal(tree.getRightChild())

def preOrderTraversal(tree):
    if tree != None:
        print(tree.getRootVal())
        preOrderTraversal(tree.getLeftChild())
        preOrderTraversal(tree.getRightChild())

def postOrderTraversal(tree):
    if tree != None:
        postOrderTraversal(tree.getLeftChild())
        postOrderTraversal(tree.getRightChild())
        print(tree.getRootVal())


def main():
    b = BinaryTree(1)
    """
        You can add a for loop here to create as many childs as you want. 
    """
    b.insertLeft(2)
    b.insertRight(3)

    print("\nInorder Traversal: L,Root,R")
    inorderTraversal(b)
    print("\nPre Order Traversal: Root,L,R")
    preOrderTraversal(b)
    print("\nPost Order Traversal: L, R, Root")
    postOrderTraversal(b)

if __name__ == '__main__':
    main()