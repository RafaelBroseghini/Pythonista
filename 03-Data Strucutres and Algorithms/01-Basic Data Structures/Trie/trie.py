class Trie(object):
    """reTRIEval Membership Data Structure"""
    class __TrieNode(object):
        def __init__(self, item, next=None, follows=None):
            self.item = item
            self.next = next
            self.follows = follows

        def setFollows(self, newFollower):
            self.follows = newFollower

        def setNext(self, newNext):
            self.next = newNext

        def getFollows(self):
            return self.follows

        def getNext(self):
            return self.next

    def __init__(self):
        self.start = None
    
    def insert(self, item):
        item += "$"
        self.start = Trie.__insert(self.start, item)
    
    def __contains__(self, item):
        item += "$"
        return Trie.__contains(self.start, item)

    def __insert(node, item):
        if len(item) == 0:
            return node
        
        if node == None:
            node = Trie.__TrieNode(item[0])

        if node.item == item[0]:
            node.setFollows(Trie.__insert(node.getFollows(), item[1:]))
        else:
            node.setNext(Trie.__insert(node.getNext(), item))

        return node
    
    def __contains(node, item):
        if len(item) == 0:
            return True
        
        if node == None:
            return False

        if node.item == item[0]:
            return Trie.__contains(node.follows, item[1:])
        else:
            return Trie.__contains(node.next, item)


def main():
    t = Trie()

    t.insert("coward")
    t.insert("cow")
    t.insert("cattle")
    t.insert("cat")
    t.insert("rat")
    t.insert("rabbit")
    t.insert("dog")

    assert "coward" in t
    assert "cow" in t
    assert "cattle" in t
    assert "cat" in t
    assert "rat" in t
    assert "rabbit" in t
    assert "dog" in t
    assert "luther" not in t
    
    # print(t.start.item)
    # print(t.start.follows.item)
    # print(t.start.follows.follows.item)
    # print(t.start.follows.follows.follows.item)
    # print()
    # test
    # print(t.start.item)
    # print(t.start.follows.item)
    # print(t.start.follows.follows.item)
    # print(t.start.follows.follows.follows.item)
    # print(t.start.follows.follows.follows.next.item)
    # # print(t.start.follows.follows.follows.next.follows.item)
    # print()
    # print(t.start.item)
    # print(t.start.follows.item)
    # print(t.start.follows.next.item)
    # print(t.start.follows.next.follows.item)
    # print(t.start.follows.next.follows.follows.item)
    # print()
    # print(t.start.item)
    # print(t.start.next.item)
    # print(t.start.next.follows.item)
    # print(t.start.next.follows.follows.item)
    # print(t.start.next.follows.follows.next.item)
    # print(t.start.next.follows.follows.next.follows.item)
    # print(t.start.next.follows.follows.next.follows.follows.item)
    # print(t.start.next.follows.follows.next.follows.follows.follows.item)
    # print(t.start.next.follows.follows.next.follows.follows.follows.follows.item)
    # print()
    # print(t.start.item)
    # print(t.start.next.item)
    # print(t.start.next.next.item)
    # print(t.start.next.next.follows.item)
    # print(t.start.next.next.follows.follows.item)
    # print(t.start.next.next.follows.follows.follows.item)
    # print()

if __name__ == '__main__':
    main()
