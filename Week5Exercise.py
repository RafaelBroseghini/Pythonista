class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def palchecker(aString):
    chardeque = Deque()
    new_String= aString.replace(' ','')

    for ch in new_String:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("IPR EFE R     PI"))
print(palchecker("r a       d ar    "))

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
from abc import ABC, abstractmethod
class LinkedList(ABC):
    @abstractmethod
    def __init__(self):
        self._head = None
        self._count = 0
    def is_empty(self):
        return self._count == 0
    def __len__(self):
        return self._count
    @abstractmethod
    def add(self, new_node):
        pass
    @abstractmethod
    def append(self, new_node):
        pass
    @abstractmethod
    def insert(self, new_node):
        pass
    @abstractmethod
    def index(self, value):
        pass
    @abstractmethod
    def remove(self):
        pass
    def pop(self, position=None):
        pass
    def __getitem__(self, rng):
        if isinstance(rng, int):
            return rng
            #return a single node
        elif isinstance(rng, slice):
            #return a slice
            slice_lst = UnorderedLinkedList()
            slice_rng = list(range(rng.start, rng.stop))
            slice_count = 0
            current = self._head
            while current and slice_count < rng.start:
                current = current.next
                slice_count += 1
            while current and slice_count < rng.stop:
                    slice_lst.append(Node(current.data))
                    current = current.next
                    slice_count += 1
        return slice_lst
        
class UnorderedLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        super().__init__()
        
    def add(self, new_node):
        '''Add a new node at the beginning of a list'''
        new_node.next = self._head
        self._head = new_node
        self._count += 1

    def append(self, new_node):
        if not self._head:
            self._head = new_node
            self._count += 1
            return
        current  = self._head
        while current.next:
            current = current.next
        current.next = new_node
        self._count += 1

    def insert(self, index, new_node):
        current = self._head
        for i in range(index):
            current = current.getNext()
        
        if current != None:
            new_item = Node(new_node)
            new_item.setNext(current.getNext())
            current.setNext(new_item)
        else:
            raise("Index out of range")  
    
    def remove(self, value):
        '''Remove a node with the specified value from a list'''
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
        while current != None:
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
            
import random
ull = UnorderedLinkedList()
for _ in range(10):
    n = Node(random.randint(1, 10))
    ull.append(n)
    print("{}: {}".format(len(ull), ull))
print('node removal')
ull.remove(5)
print("{}: {}".format(len(ull), ull))
ull.insert(4, 27)
print(ull)
ull.pop(3)
print(ull)
print(ull.index(27))


class OrderedList:
    
    def __init__(self):
        self._head = None

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self._head
        previous = None
        stop = False
        while current != None and not stop:
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
            
    def remove(self,item):
        current = self._head
        previous = None
        found = False
        stop = False
        while not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self._head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def getItem(self, index):
        current = self._head
        for i in range(index):
            current = current.getNext()
        if current != None:
            return current.getData()
        else:
            raise("Index out of range.")
        
    def index(self, item):
        index = 0
        current = self._head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            print('Value of ' + str(item) +' does not return an index because it is not in this list.')
        return 'Index of ' + str(item) + ' is: ' + str(index)
        
    def pop(self, index):
        try:
            if index != -1:
                self.remove(self.getItem(index))
            else:
                index = self.size() - 1
                self.remove(self.getItem(index))
        except Exception as ie:
            print('Index out of range for pop method.')
            
    def isEmpty(self):
        return self._head == None

    def size(self):
        current = self._head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def insert(self, index, item):
        current = self._head
        for i in range(index):
            current = current.getNext()
 
        if current != None:
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
        else:
            raise("Index out of range")

    def append(self, new_node):
        if not self._head:
            self._head = new_node
            return
        current  = self._head
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

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
try:
    mylist.pop(9)
except Exception as ie:
    print(ie)
mylist.insert(0, 2)
print(mylist)
print(mylist.index(17)) 
n = Node(5)
mylist.append(n)
print(mylist)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

