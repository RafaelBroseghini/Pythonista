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


class OrderedList:
    def __init__(self):
        self._head = None

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self._head)
            self._head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                print(current.getData())
        if previous is None:
            self._head = current.getNext()
        else:
            previous.setNext(current.getNext())

        if current is None:
            print("Index out of range")

    def getItem(self, index):
        current = self._head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.getNext()
        if current is not None:
            return current.getData()
        else:
            raise IndexError

    def index(self, item):
        index = 0
        current = self._head
        found = False
        while current is not None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            print(
                "Value of "
                + str(item)
                + " does not return an index because it is not in this list."
            )
        return "Index of " + str(item) + " is: " + str(index)

    def pop(self, index):
        try:
            if index != -1:
                self.remove(self.getItem(index))
            else:
                index = self.size() - 1
                self.remove(self.getItem(index))
        except IndexError:
            print("Index out of range for pop method.")

    def isEmpty(self):
        return self._head == None

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def insert(self, index, item):
        current = self._head
        for i in range(index):
            current = current.getNext()

        if current is not None:
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
        else:
            raise ("Index out of range")

    def append(self, new_node):
        if not self._head:
            self._head = new_node
            return
        current = self._head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        all_nodes = []
        current = self._head
        while current:
            all_nodes.append(current.data)
            current = current.next
        return str(all_nodes)


def main():
    lst = OrderedList()
    vals = [31, 2, 5, 1, 235, 5, 23, 4, 5, 5, 234, 3, 42, 34, 5, 66]
    for val in vals:
        lst.add(val)
    lst.pop(9)
    lst.insert(0, 2)
    print(lst)
    print(lst.index(17))
    n = Node(5)
    lst.append(n)
    print(lst)

    print(lst.size())
    print(lst.search(93))
    print(lst.search(100))


if __name__ == "__main__":
    main()
