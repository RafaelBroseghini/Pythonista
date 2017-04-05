'''
Name: Rafael Broseghini
Prof: Roman Yasinovskyy

Date: 04/01/2017
Filename: Week8ProjectBroseghini.py
'''

class Map:
    def __init__(self, size = 8):
        self._items = [None] * size
        self._size = size
        self._keys = set()
        
    def rehash(self, key, k=0):
        return (key % self._size + k * k) % self._size
        
    def put(self, key, val):
        pos = self.rehash(key)
        if not self._items[pos]:
            self._items[pos] = (key, val)
            self._keys.add(key)
        else:
            for k in range(self._size):
                pos = self.rehash(key, k)        
                if not self._items[pos]:
                    self._keys.add(key)
                    self._items[pos] = (key, val)
                    break
                elif self._items[pos][0] == key:
                    self._items[pos] = (key, val)
                    break
    
    def get(self, key):
        if not key in self._keys:
            raise TypeError('Key ' + str(key) + ' is not in the map, therefore it is not possible to retrieve a value.')
        else:
            for k in range(self._size):
                if self._items[k]:
                    if self._items[k][0] == key:
                        return self._items[k][1]
               
        
            
    def __contains__(self, key):
        return key in self._keys
        
    def __len__(self):
        result = 0
        for _ in self._items:
            if _:
                result += 1
        return result
    
    def __str__(self):
        return str([i for i in self._items if i])
m = Map()
m.put(33, 'Alice')
print('Map:', m)
print("Items in the map: {}".format(len(m)))
print()
m.put(35, 'Bob')
m.put(26, 'Chuck')
m.put(46, 'Number')
m.put(28, 'Rafael')
m.put(88, 'Maria')
m.put(433, 'Meme')
m.put(22, 'Soccer')
m.put(77, 'Lion')
m.put(95, 'Peter')
m.put(25, 'Null')
m.put(87, 'Wow')
m.put(100, 'Jesus')
print('Map:', m)
print("Items in the map: {}".format(len(m)))
m.put(74, 'Bye')
print()
print('Map:', m)
print("Items in the map: {}".format(len(m)))
print()
print("Is key 11 in the map? {}".format(11 in m))
print("Is key 33 in the map? {}".format(33 in m))
print("Is key 35 in the map? {}".format(35 in m))
print("Is key 74 in the map? {}".format(74 in m))
print("Is key 99 in the map? {}".format(99 in m))
print()
for i in [33, 22, 25, 11, 35, 74, 95, 77, 123, 26, 28, 47, 56, 88, 46, 87, 100, 433]:
    try:
        print('Value of key ' + str(i) +': {}'.format(m.get(i)))
        print()
    except TypeError as ie:
        print(ie)
        print()




