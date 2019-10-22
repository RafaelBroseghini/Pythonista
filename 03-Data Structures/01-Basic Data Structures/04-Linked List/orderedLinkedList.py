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