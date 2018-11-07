class Stack(object):
    """docstring for Stack."""
    def __init__(self):
        self.items = []
        
    # push element on to the stack.
    def push(self, item):
        self.items.append(item)
        
    # pop element from the stack.
    def pop(self):
        return self.items.pop()
        
    # peek element at top of the stack. Will throw error if empty.
    def peek(self):
        return self.items[len(self.items)-1]
    
    # Boolean True if stack is empty.
    def isEmpty(self):
        return len(self.items) == 0
    
    # Numbers of element in the stack.
    def size(self):
        return len(self.items)



s = Stack()
