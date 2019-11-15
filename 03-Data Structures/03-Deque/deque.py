"""
ASSUMING LEFT IS TOP. AND RIGHT IS END.
"""


class Deque(object):
    """docstring for Deque."""

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        self.items.pop(0)

    def removeRear(self):
        self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


d = Deque()

d.addFront(99)
d.addFront(89)
d.addFront(79)

d.addRear(199)

d.removeFront()

d.removeRear()

print(d.items)
