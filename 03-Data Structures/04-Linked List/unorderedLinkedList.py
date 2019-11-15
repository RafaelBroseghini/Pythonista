import random


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        super().__init__()

    def add(self, new_node):
        """Add a new node at the beginning of a list"""
        new_node.next = self._head
        self._head = new_node
        self._count += 1

    def append(self, new_node):
        if not self._head:
            self._head = new_node
            self._count += 1
            return
        current = self._head
        while current.next:
            current = current.next
        current.next = new_node
        self._count += 1

    def insert(self, index, new_node):
        current = self._head
        for i in range(index):
            current = current.getNext()

        if current is not None:
            new_item = Node(new_node)
            new_item.setNext(current.getNext())
            current.setNext(new_item)
        else:
            raise ("Index out of range")

    def remove(self, value):
        """Remove a node with the specified value from a list"""
        prev = None
        current = self._head
        while current and current.data != value:
            prev = current
            current = current.next
        if current:
            if prev:
                prev.next = current.next
            else:
                self._head = current.next
            del current
            self._count = self._count - 1

    def pop(self, rng):
        self.remove(self.__getitem__(rng))

    def index(self, value):
        index = 0
        current = self._head
        found = False
        while current is not None:
            if current.getData() == value:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = None
        return index

    def __str__(self):
        all_nodes = []
        current = self._head
        while current:
            all_nodes.append(current.data)
            current = current.next
        return str(all_nodes)


ull = UnorderedLinkedList()
for _ in range(10):
    n = Node(random.randint(1, 10))
    ull.append(n)
    print("{}: {}".format(len(ull), ull))
print("node removal")
ull.remove(5)
print("{}: {}".format(len(ull), ull))
ull.insert(4, 27)
print(ull)
ull.pop(3)
print(ull)
print(ull.index(27))
