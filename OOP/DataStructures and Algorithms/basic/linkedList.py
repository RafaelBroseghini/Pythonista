import random



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


    """
        These methods below are for experimentation purposes.


        -----------------------------------------------------
    """

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def getMiddleElem(self):

        """
            This method depends if size is even or odd. Need consensus.
        """

        current = self.head
        i = 1
        while i < self.size() // 2:
            current = current.next
            i += 1
        return current
    
    def printLinkedList(self):
        current = self.head

        print("\nHead is: {}".format(current.data))
        while current.next != None:
            print(current.data, current.next.data)
            current = current.next
        print(current.data, current.next)
        print()


def main():
    
    random.seed(11)

    l = LinkedList()
    for item in range(1,11):
        l.add2Head(item+random.randint(32,876))


    print("Size: ", l.size())
    print("Middle Elem:",l.getMiddleElem().data)

    l.printLinkedList()

    print("Removed head: {}".format(l.removeFromHead().data))

    l.printLinkedList()
if __name__ == '__main__':
    main()
