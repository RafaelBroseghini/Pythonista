class Stack(object):
    """docstring for Stack."""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)



s = Stack()
