# RAFAEL BROSEGHINI
# CS 160

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
s = Stack()
def rpn_calc():
    expr = input('Enter Reverse Polish notation expression: ')
    for token in expr.split():
        if len(expr.split()) % 2 != 0:
            raise IndexError('Too few operands in the expression.')
        elif '=' in expr:
            if token == '=':
                try:
                    result = s.pop()
                except IndexError as ie:
                    print('Caught an error: {}'.format(ie))
                if s.isEmpty():
                    print(result)
                else:
                    raise IndexError("Too many this expression")
        elif token == "*":
            op1 = s.pop()
            op2 = s.pop()
            s.push(op2 * op1)
        elif token == '+':
            op1 = s.pop()
            op2 = s.pop()
            s.push(op2 + op1)
        elif token == '-':
            op1 = s.pop()
            op2 = s.pop()
            s.push(op2 - op1)        
        else:
            s.push(int(token))
    else:
        raise IndexError('You need an equal sign in the expression')

def read_expressions():    
    with open('expressions2.txt', 'r') as exp:
        par_list = list()
        for line in exp.readlines():
            line_item = line.strip('\n')
            par_list.append(line_item)
        return par_list
    

'''try:
    for i in read_expressions():
        rpn_calc(i)    
except (IndexError, IndexError, IndexError, IndexError) as ie:
    print(ie)
#for i in read_expressions():
 #   print(i)'''

print(rpn_calc())
