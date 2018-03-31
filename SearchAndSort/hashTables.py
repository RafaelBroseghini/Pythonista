def hashing(arr,elem):
    pos = elem % len(arr)
    arr[pos] = elem

    return arr

def findElem(elem,arr):
    slot = elem % len(arr)
    if arr[slot] == elem:
        return True
    return False


print("Functional Programming of HashTable:\n")
arr = [None] * 11
temp = [54,26,93,17,77,31]

for item in temp:
    hashing(arr,item)

print("Elem {} is in {} ?: {}".format(54,arr,findElem(54,arr)))
print("Elem {} is in {} ?: {}\n".format(88,arr,findElem(88,arr)))




"""OOP implementation of Hash Table
   Not using rehashing. Simply put and get."""

class HashTable(object):
    def __init__(self, size):
        self.table = [None] * size

    def hash(self, elem):
        slot = elem % len(self.table)

        self.table[slot] = elem

    def find(self, elem):
        slot = elem % len(self.table)
        if self.table[slot] == elem:
            return True

        return False

    def __repr__(self):
        return repr(self.table)


print("OOP implementation of HashTable:\n")
ht = HashTable(11)

for item in temp:
    ht.hash(item)

print("Elem {} is in {} ?: {}".format(54,ht.table,ht.find(54)))
print("Elem {} is in {} ?: {}".format(88,ht.table,ht.find(88)))
