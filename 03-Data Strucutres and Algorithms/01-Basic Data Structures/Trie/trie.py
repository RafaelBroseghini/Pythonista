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

    def suggest(self, item):
      if item in self:
        return None

      item += "$"
      return Trie.__suggestions(self.start, item)

    def __suggestions(node, item, word="", parent=None):
      if node == None:
        current = parent 
        while current.follows.item != "$":
          word += current.follows.item
          current = current.follows

      elif node.item == item[0]:
        parent = node
        word += node.item
        return Trie.__suggestions(node.follows, item[1:], word, parent)
    
      else:
        return Trie.__suggestions(node.next, item, word, parent)
      
      return word


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
    
    print(t.suggest("ca"))

if __name__ == '__main__':
    main()