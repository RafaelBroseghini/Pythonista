class BinHeap(object):
    def __init__(self):
        self.heaplist = []
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                temp = self.heaplist[i // 2]

                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = temp
            i = i // 2

    def insert(self, k):
        self.heaplist.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i*2) <= self.currentSize:

            mc = self.maxChild(i)
            print("The max child is at index: ", mc)
            if self.heaplist[i] < self.heaplist[mc]:
                print("Swapping {} with {}".format(self.heaplist[i], self.heaplist[mc]))
                temp = self.heaplist[i]

                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = temp
                print(self.heaplist)

            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2 - 1
        else:
            if self.heaplist[i*2] > self.heaplist[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMax(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(0)
        return retval

    def buildHeap(self, lst):
        i = len(lst) // 2
        self.currentSize = len(lst)
        self.heaplist = lst[:]

        print("Initial list {}".format(self.heaplist))
        while (i >= 0):
            print("The percolating is starting from index: {}, which is number {}.".format(i,self.heaplist[i]) )
            self.percDown(i)
            print(self.heaplist)
            i -= 1

bh = BinHeap()

lst = [1,2,3,4,5,6,7,100,9,10,12,42,77,55]

bh.buildHeap(lst)
