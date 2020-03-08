"""Depth First Search, Recursively on a Tree Structure."""


class Tree(object):
    class _Node(object):
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            self.parent = None

        def getVal(self):
            return self.val

        def getParent(self):
            return self.parent

        def inorder(self):
            if self.left is not None:
                for item in self.left.inorder():
                    yield item
            yield self
            if self.right is not None:
                for item in self.right.inorder():
                    yield item

        def __str__(self):
            return str([x.val for x in self.inorder()])

    def __init__(self, root):
        self.root = Tree._Node(root)

    def search(self, value):
        return Tree.dfs(self.root, value)

    @staticmethod
    def dfs(node, target) -> bool:
        if node:

            if node.getVal() == target:
                return True

            left = Tree.dfs(node.left, target)
            right = Tree.dfs(node.right, target)

            return left or right
        return False

    def __str__(self):
        return str(self.root)


if __name__ == "__main__":
    tree = Tree(10)
    tree.root.left = Tree._Node(5)
    tree.root.right = Tree._Node(28)
    tree.root.right.left = Tree._Node(66, left=Tree._Node(99), right=Tree._Node(100))
    tree.root.right.right = Tree._Node(8, left=Tree._Node(65), right=None)
    tree.root.left.left = Tree._Node(12, left=Tree._Node(900), right=None)
    tree.root.left.right = Tree._Node(13, left=Tree._Node(123), right=Tree._Node(43))

    print("**Inorder Traversal")
    print(tree)
    print("**Done Traversing.")

    print("\n**Running 10 tests.")
    assert tree.search(13)
    assert tree.search(28)
    assert tree.search(99)
    assert tree.search(100)
    assert tree.search(65)
    assert tree.search(12)
    assert tree.search(123)
    assert tree.search(43)
    assert not tree.search(0)
    assert not tree.search(63)
    assert not tree.search(98)
    assert not tree.search(11)
    assert not tree.search(27)
    print("**Passed all tests.")
