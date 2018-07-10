import unittest

class MaxHeap(object):
    def __init__(self):
        self.heapList = []
        self.currentsize = 0

    def insert(self, item):
        self.heapList.append(item)
        self.currentsize += 1
        print("percolating now: ", self.currentsize - 1)
        self.percUp(self.currentsize-1)
    
    def percUp(self, i):
        while i // 2  > 0:
            if self.heapList[i] > self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i //2
    
    def percDown(self, i):
        while (i*2) <= self.currentsize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2 - 1
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMax(self):
        self.heapList[1] = self.heapList[self.currentsize]
        self.currentsize -= 1
        self.percDown(0)
        self.heapList.pop()
    
    def buildHeap(self, array):
        i = len(array) // 2
        self.currentsize = len(array)
        self.heapList = array[:]

        while i >= 0:
            self.percDown(i)
            i -= 1

b = MaxHeap()

b.insert(1)
b.insert(2)
b.insert(4)
b.insert(5)
b.insert(6)
b.insert(7)
b.insert(8)
b.insert(9)
b.insert(10)



# lst = [1,2,3,4,5,6,7,100,9,10,12,42,77,55]

# b.buildHeap(lst)

print(b.heapList)