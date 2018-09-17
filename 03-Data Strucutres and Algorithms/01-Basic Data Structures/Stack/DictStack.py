class DictStack(object):
    def __init__(self):
        self.items = {}
        self.topItem = 0
    
    def push(self, item):
        self.items[self.topItem] = item
        self.topItem += 1
    
    def pop(self):
        if not self.isEmpty():
            rv = self.items[self.topItem-1]
            self.topItem -= 1
            del self.items[self.topItem]
            return rv
        
        raise Exception("DictStack is empty!")
    
    def isEmpty(self):
        return self.topItem <= 0


def main():
    s = DictStack()
    for i in range(1,11):
        s.push(i)
    
    for i in range(1,11):
        print(s.pop())
    
    print(s.pop())

if __name__ == '__main__':
    main()
