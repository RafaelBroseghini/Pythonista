"""Depth First Search, Recursively on a Tree Structure."""


class Tree(object):
    class _Node(object):
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            self.visited = False
            self.parent = None

        def getVal(self):
            return self.val

        def getParent(self):
            return self.parent

        def hasBeenVisited(self):
            return self.visited

        def setVisited(self, newVal):
            self.visited = newVal

        def setParent(self, newParent):
            if type(newParent) != type(self):
                raise TypeError("Parent has to be a _Node")
            self.parent = newParent

        def inorder(self):
            if self.left != None:
                for item in self.left.inorder():
                    yield item
            yield self
            if self.right != None:
                for item in self.right.inorder():
                    yield item

        def __str__(self):
            return str(self.val)

        def __iter__(self):
            return self.inorder()

    def __init__(self, root):
        self.root = Tree._Node(root)

    def clear(self):
        for item in self:
            item.setVisited(False)

    def search(self, value):
        self.clear()
        return Tree.dfs(self.root, value)

    def dfs(node, target) -> bool:
        if node == None:
            return False

        if node.getVal() == target:
            return True

        children = [node.left, node.right]

        for child in children:
            if child != None:
                if not child.hasBeenVisited():
                    child.setVisited(True)
                    child.setParent(node)
                    return Tree.dfs(child, target)

        return Tree.dfs(node.getParent(), target)

    def __iter__(self):
        return iter(self.root)


if __name__ == "__main__":
    tree = Tree(10)
    tree.root.left = Tree._Node(5)
    tree.root.right = Tree._Node(28)
    tree.root.right.left = Tree._Node(66, left=Tree._Node(99), right=Tree._Node(100))
    tree.root.right.right = Tree._Node(8, left=Tree._Node(65), right=None)
    tree.root.left.left = Tree._Node(12, left=Tree._Node(900), right=None)
    tree.root.left.right = Tree._Node(13, left=Tree._Node(123), right=Tree._Node(43))

    print("**Inorder Traversal")
    for node in tree:
        print(node)
    print("**Done Traversing.")

    print("\n**Running 10 tests.")
    assert tree.search(13)
    assert tree.search(28)
    assert tree.search(99)
    assert tree.search(100)
    assert tree.search(65)
    assert not tree.search(0)
    assert not tree.search(63)
    assert not tree.search(98)
    assert not tree.search(11)
    assert not tree.search(27)
    print("**Passed all tests.")
