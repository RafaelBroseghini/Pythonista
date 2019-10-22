   
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(len(self.items)-1)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        val = ""

        for i in range(len(self.items)-1,-1,-1):
            itemStr = str(self.items[i])
            val += itemStr + "\n" + "-"*len(itemStr) + "\n"

        val += "BOTTOM"
        return val


      