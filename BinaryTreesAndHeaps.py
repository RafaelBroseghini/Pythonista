'''
Name: Rafael Broseghini
Prof: Roman Yasinovskyy

Filename: BinaryTreesAndHeaps.py
Date: 04/20/2017
'''


# Task 1
def BinaryTreeLst(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def build_tree_lst():
    r = BinaryTreeLst('a')
    insertLeft(r,'b')
    insertRight(r, 'c')
    l = getLeftChild(r)
    p = getRightChild(r)
    insertRight(l,'d')
    insertLeft(p, 'e')
    insertRight(p, 'f')
    print(r)

def main():
    print()
    print('Task 1:')
    print('Creating a tree that uses textbook implementation of a tree as a list of lists:')
    build_tree_lst()
    print()
main()






# Task 2
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    # Task 3
    def height(self):
        if self.key == None:
            return 0
        return max(self.leftChild.height() if self.leftChild is not None else 0, self.rightChild.height() if self.rightChild is not None else 0) + 1    
    
    def __str__(self):
        return str(self.key)

def build_tree_oop():
    print('Task 2:')
    print('Creating a tree that uses textbook implementation of a tree as nodes and references:')
    print('See build_tree_oop() function.') 
    print()
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')
    r.getLeftChild().insertRight('d')
    print('Task 3:')
    print('The height of the Binary Tree built within build_tree_oop() is:', r.height())    
build_tree_oop()

class MaxHeap:
    def __init__(self, n=0):
        self._items = []
        self._size = n
        

    def is_empty(self):
        return self._items == []

    def is_full(self):
        return len(self._items) >= self._size

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def insert(self, item):
        self._items.append(item)
        self.percUp(len(self._items)-1)

    def percUp(self, current):
        while (current - 1) // 2 >= 0:
            parent = (current - 1) // 2
            if self._items[current] < self._items[parent]:
                self._items[current], self._items[parent] = self._items[parent], self._items[current]
            else:
                return
            current = parent

    def get_min_child(self, parent):
        if 2 * parent + 2 > len(self._items) - 1:
            return 2 * parent + 1
        else:
            if self._items[2 * parent + 1] > self._items[2 * parent + 2]:
                return 2 * parent + 1
            else:
                return 2 * parent + 2    

    def percDown(self, current):
        while 2*current + 1 < len(self._items):
            smaller_index = self.get_min_child(current)
            if self._items[current] < self._items[smaller_index]:
                self._items[current], self._items[smaller_index] = self._items[smaller_index], self._items[current]
            else:
                return
            current = smaller_index

    def delete(self):
        self._items[0], self._items[len(self._items)-1] = self._items[len(self._items)-1], self._items[0]
        res = self._items.pop()
        self.percDown(0)
        return res


    def build_heap(self, lst):
        self._items = lst[:]
        current = len(self._items) // 2 - 1
        while current >= 0:
            self.percDown(current)
            current = current - 1
            
            
            
            
my_heap = MaxHeap()
lst = [10, 24, 21, 300, 2, 77, 99, 1995, 235, 122, 413, 89, 9, 43, 872, 54, 93]
my_heap.build_heap(lst)
print()
print('Task 4:')
print('Max Heap implementation', my_heap)

class MaxHeapLimitedSize:
    def __init__(self, n=7, items= []):
        self._items = []
        self._size = n
        

    def is_empty(self):
        return self._items == []

    def is_full(self):
        return len(self._items) >= self._size

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def insert(self, item):
        self._items.append(item)
        self.percUp(len(self._items)-1)

    def percUp(self, current):
        while (current - 1) // 2 >= 0:
            parent = (current - 1) // 2
            if self._items[current] < self._items[parent]:
                self._items[current], self._items[parent] = self._items[parent], self._items[current]
            else:
                return
            current = parent

    def get_min_child(self, parent):
        if 2 * parent + 2 > len(self._items) - 1:
            return 2 * parent + 1
        else:
            if self._items[2 * parent + 1] > self._items[2 * parent + 2]:
                return 2 * parent + 1
            else:
                return 2 * parent + 2    

    def percDown(self, current):
        while 2*current + 1 < len(self._items):
            smaller_index = self.get_min_child(current)
            if self._items[current] < self._items[smaller_index]:
                self._items[current], self._items[smaller_index] = self._items[smaller_index], self._items[current]
            else:
                return
            current = smaller_index

    def delete(self):
        self._items[0], self._items[len(self._items)-1] = self._items[len(self._items)-1], self._items[0]
        res = self._items.pop()
        self.percDown(0)
        return res


    def build_heap(self, lst):
        self._items = lst[:]
        while len(self._items) > self._size:
            self._items.remove(min(self._items))
        current = len(self._items) // 2 - 1
        while current >= 0:
            self.percDown(current)
            current = current - 1
            
def main():            
    my_heap = MaxHeapLimitedSize()
    lst = [10, 24, 21, 300, 2, 77, 99, 1995, 235, 122, 413, 89, 9, 43, 872, 54, 93]
    my_heap.build_heap(lst)
    print()
    print('Task 5:')
    print('Max Heap with limited size of 7:', my_heap)
    #print('Largest item in Max Heap with limited size of 7:', my_heap.delete())
    #print('New Max Heap after deleting largest value:', my_heap)
main()
