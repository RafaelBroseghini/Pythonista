class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList(object):
    """docstring for LinkedList."""
    def __init__(self):
        self.head = None

    def add2Head(self, item):
        item = Node(item)
        item.next = self.head
        self.head = item

    def add2Tail(self, item):
        item = Node(item)

        current = self.head
        while current.next != None:
            current = current.next
        current.next = item

    def removeFromHead(self):
        current = self.head
        self.head = self.head.next
        return current


l = LinkedList()
for item in range(1,11):
    l.add2Head(item)


current = l.head

print("Head is {}".format(current.data))
while current.next != None:
    print(current.data, current.next.data)
    current = current.next
print(current.data, current.next)


print("Removed head: {}".format(l.removeFromHead().data))
current = l.head

print("Head is {}".format(current.data))
while current.next != None:
    print(current.data, current.next.data)
    current = current.next
print(current.data, current.next)
