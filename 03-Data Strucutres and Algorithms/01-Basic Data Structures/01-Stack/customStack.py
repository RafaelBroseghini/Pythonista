class Stack(object):
    """
    Stack ADT with additional methods:
    transfer, clear (recursive).
    """
    def __init__(self):
        self.items = []
        
    # push element on to the stack.
    def push(self, item):
        self.items.append(item)
        
    # pop element from the stack.
    def pop(self):
        return self.items.pop()
    
    # Transfer items from one stack into another.
    def transfer(self, other):
        if not isinstance(other, Stack):
            raise Exception("Cannot transfer to a non-Stack object.")

        while not self.isEmpty():
            item = self.pop()
            other.push(item)
    
    # Empty the stack recursively.
    def clear(self):
        if self.isEmpty():
            return self.items
        else:
            self.pop()
            return self.clear()

    # peek element at top of the stack. Will throw error if empty.
    def peek(self):
        return self.items[len(self.items)-1]
    
    # Boolean True if stack is empty.
    def isEmpty(self):
        return len(self.items) == 0
    
    # Numbers of element in the stack.
    def size(self):
        return len(self.items)

# Reverse the current stack using a temp list (acts as queue)
def reverse(s1):
    temp = []

    while not s1.isEmpty():
        temp.insert(0, s1.pop())
    
    while not len(temp) == 0:
        s1.push(temp.pop())

# Reverse a given stack using two additional stacks.
def reverse_using_two_stacks(s1):
    temp1 = Stack()
    temp2 = Stack()

    while not s1.isEmpty():
        temp1.push(s1.pop())
    
    while not temp1.isEmpty():
        temp2.push(temp1.pop())

    while not temp2.isEmpty():
        s1.push(temp2.pop())
        

def push_all(s1, stop):
    for i in range(1, 11):
        s1.push(i)

def main():
    s1 = Stack()
    s2 = Stack()
    s3 = []

    push_all(s1, 11)

    print("Stack 1 before transfer:", s1.items)
    print("Stack 2 before transfer:", s2.items)
    s1.transfer(s2)

    print("Stack 1 after transfer: ", s1.items)
    print("Stack 2 after transfer: ", s2.items)

    push_all(s1, 11)

    print("Stack 1 before clearing:", s1.items)

    s1.clear()

    print("Stack 1 after clearing:", s1.items)

    push_all(s1, 11)

    print("Stack 1 before reversing:", s1.items)

    reverse(s1)

    print("Stack 1 after reversing:", s1.items)

    # Here we reverse the stack again to
    # put items back in order.
    reverse(s1)

    print("Stack 1 before reversing using two addtional stacks:", s1.items)
    
    reverse_using_two_stacks(s1)

    print("Stack 1 after reversing using two addtional stacks:", s1.items)

if __name__ == '__main__':
    main()
