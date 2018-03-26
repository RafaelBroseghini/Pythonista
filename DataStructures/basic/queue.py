class Queue(object):
    """docstring for Queue."""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return  len(self.items)


q = Queue()
