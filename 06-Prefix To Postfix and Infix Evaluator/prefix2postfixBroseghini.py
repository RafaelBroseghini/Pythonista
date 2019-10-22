'''
Name: Rafael Broseghini
Prof: Kent Lee

Course: CS 260
Date: 10/27/2017
'''
# LL(1) GRrammar
# Suitable for Top-Down Parser
# Prog -> E eof
# E -> + E E | * E E | S E | R | num
# G = (Non-terminals, Terminals (i.e. tokens), Productions, Start Symbol)
# G = ({E, Prog}, {+, *, S, R, num, eof}, P(given by line 3 and 4), Prog)

import io
import streamreader

memory = [0]


class MulNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return " ".join([str(self.left.eval()), str(self.right.eval()),"*"])


class AddNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
       
        return " ".join([str(self.left.eval()), str(self.right.eval()),"+"])

 
class SubtractNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return " ".join([str(self.left.eval()), str(self.right.eval()),"-"])
    
class DivideNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return " ".join([str(self.left.eval()), str(self.right.eval()),"/"])
    
class StoreNode:

    def __init__(self, child):
        self.child = child

    def eval(self):
        memory[0] = self.child.eval()
        return memory[0]


class RecallNode:

    def __init__(self):
        pass

    def eval(self):
        return memory[0]

class NumNode:
    def __init__(self, num):
        self.val = num

    def eval(self):
        return self.val

def Prog(reader):
    ast = E(reader)
    token = reader.getToken()
        
    if reader.eof():
        return ast
    
    raise Exception("Invalid Prefix expression") 

def E(reader):
    token = reader.getToken()
    
    if token == "*":
        left = E(reader)
        right = E(reader)
        return MulNode(left, right)
    
    if token == "+":
        left = E(reader)
        right = E(reader)
        return AddNode(left, right)
    
    if token == "-":
        left = E(reader)
        right = E(reader)
        return SubtractNode(left, right)
    
    if token == '/':
        left = E(reader)
        right = E(reader)
        return DivideNode(left, right)
    
    if token == "S":    
        return StoreNode(E(reader))

    if token == "R":
        return RecallNode()
    
    try:
        v = int(token)
        return NumNode(v)
    
    except ValueError:
        raise Exception("Invalid Prefix expression: " + token)  

def main():
    expression = input('Please enter a prefix Expression (or press enter to stop): ').strip()
    
    while expression!="":
        
        #use streamreader over the string entered to get the tokens of the string.
        reader = streamreader.StreamReader(io.StringIO(expression))
        
        try:
            
            #ast will be the abstract syntax tree. Prog (parse) is called on reader
            ast = Prog(reader)
            
            #print the postfix notation.
            print(ast.eval())
        except Exception as e:
            print(e)        
        
        
        expression = input('Please enter a prefix Expression (or press enter to stop): ').strip()  

if __name__=="__main__":
    main()