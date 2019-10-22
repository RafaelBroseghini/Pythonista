class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    """docstring for LinkedList."""
    def __init__(self):
        self.head = Node(None)
        self.trailer = Node(None)

        self.head.next = self.trailer

    def insert2Head(self, item):
        item = Node(item)

        item.prev = self.head
        item.next = self.head.next

        self.head.next.prev = item
        self.head.next = item

    def insertAtIndex(self, target, item):
        if target == 0:
            self.insert2Head(item)

        current = self.head
        item = Node(item)

        for i in range(0,target+1):
            current = current.next

        item.prev = current.prev
        item.next = current

        current.prev.next = item
        current.prev = item


d = DoublyLinkedList()

d.insert2Head(99)
d.insert2Head(10)

d.insertAtIndex(1,100)


print("Header {}".format(d.head.data))
print("Header next {}".format(d.head.next.data))
print(d.head.next.next.data)
print(d.head.next.next.next.data)

print("Trailer {}".format(d.trailer.data))
print("Trailer prev {}".format(d.trailer.prev.data))
