import random

'''
Name: Rafael Broseghini
Prof: Roman Yasinovskyy

Date: 04/01/2017
Filename: Week8ProjectBroseghini.py
'''

class Map(object):
    def __init__(self, size = 8):
        self._keys = [None] * size
        self._data = [None] * size
        self._size = size
        
    def hashFn(self, key):
        return key % self._size

    def rehash(self, key, k=0):
        return ((key % self._size) + k) % self._size
    

    def put(self, key, val):
        pos = self.hashFn(key)
        if not self._keys[pos]:
            self._keys[pos] = key
            self._data[pos] = val
        else:
            placed = False
            i = 0
            while not placed and i < self._size:
                pos = self.rehash(key, i)
                print(val, pos)
                if not self._keys[i]:
                    self._keys[i] = key
                    self._data[i] = val
                    placed = True
                
                i += 1

    def get(self, key):
        pos = self.hashFn(key)
        if self._keys[pos] == key:
            return self._data[pos]
        else:
            i = 0
            while i < self._size:
                pos = self.rehash(key, i)

                if self._keys[pos] == key:
                    return self._data[pos]
                
                i += 1
            
            return False

            
    def __contains__(self, key):
        return key in self._data
        
    def __len__(self):
        result = 0
        for _ in self._keys:
            if _:
                result += 1
        return result
    
    def __str__(self):
        return str([i for i in self._data])

def main():
    m = Map()

    m.put(21,"this")
    m.put(21,"is")
    m.put(21,"a")
    m.put(21,"mini")
    m.put(21,"version")
    m.put(21,"of")
    m.put(21,"a")
    m.put(21,"poem")

    print(m.get(28))
    print(m)
if __name__ == '__main__':
    main()




