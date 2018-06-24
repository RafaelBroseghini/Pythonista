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

        
def read_expressions():    
    with open('rpnexpressions.txt', 'r') as exp:
        expr_list = list()
        for line in exp.readlines():
            line = line.strip('\n')
            expr_list.append(line)
        return expr_list

def evaluate_expr(expr):
    if len(expr.split()) % 2 != 0:
        raise IndexError('Too few/many operands in the expression.')

    elif '=' not in expr:
        raise IndexError('You need an equal sign in the expression.')

    return expr

def rpn_calc(expression, s):
    for token in expression.split():

        """ '=' never gets pushed into the stack. 
            It serves the purpose to grab the second to last element in the stack and 
            print to standard output. 
        """
        if token == "*":
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
        elif token == '/':
            op1 = s.pop()
            op2 = s.pop()
            s.push(op2 / op1)  
        elif token == '=':
            result = s.pop()
            if s.isEmpty():
                return "{}in rpn =: {}\n".format(expression[:len(expression)-1],int(result))
            else:
                raise Warning("Stack is not empty even though there are even amount of tokens in it.")
        else:
            s.push(int(token))

def main():
    s = Stack()
    all_expr = read_expressions()
    for expression in all_expr:
        print(rpn_calc(evaluate_expr(expression), s))

if __name__ == '__main__':
    main()
