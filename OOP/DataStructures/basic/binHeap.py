class BinHeap(object):
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
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

            mc = self.minChild(i)
            print("The min child is at index: ", mc)
            if self.heaplist[i] > self.heaplist[mc]:
                print("Swapping {} with {}".format(self.heaplist[i], self.heaplist[mc]))
                temp = self.heaplist[i]

                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = temp
                print(self.heaplist)

            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, lst):
        i = len(lst) // 2
        self.currentSize = len(lst)
        self.heaplist = [0] + lst[:]

        print("Initial list {}".format(self.heaplist))
        while (i != 0):
            print("The percolating is starting from index: {}, which is number {}.".format(i,self.heaplist[i]) )
            self.percDown(i)
            print(self.heaplist)
            i -= 1

b = BinHeap()

lst = [4,3,2,1]


b.buildHeap(lst)
