import unittest

class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, key):
        # Simple append. Increase size. Percolate that item up.
        self.heapList.append(key)
        self.currentSize += 1
        i = self.currentSize
        self.percUp(i)

    def percUp(self, i):
        # We may need to percolate the item all the way.
        # Please note that parents are at index//2.
        # Compare current index with index//2 and perform swap if necessary.
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
            i = i // 2
    
    def percDown(self, i):
        # We only need to go until len(heapList)//2 since at that point
        # it is the level of nodes before last.
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i += 1

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2 + 1
        else:
            # Comparing two children and return index of smaller one.
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        # Reassing min item to top.
        # Decrease size.
        # Percolate that item down.
        # pop repeated instance from end of heapList.
        self.heapList[1] = self.heapList[self.currentSize]  
        self.currentSize -= 1
        self.percDown(1)
        self.heapList.pop()

    def buildHeap(self, array):
        i = len(array) // 2
        self.currentSize = len(array)
        self.heapList = [0] + array[:]
        while i > 0:
            self.percDown(i)
            i -= 1
            

class Tester(unittest.TestCase):
    def test_BinHeap(self):
        b = BinHeap()
        b.insert(8)
        b.insert(1)
        b.insert(7)
        b.insert(6)
        b.insert(5)
        b.insert(3)
        self.assertEqual(b.heapList, [0,1,5,3,8,6,7])
    
if __name__ == '__main__':
    unittest.main()
