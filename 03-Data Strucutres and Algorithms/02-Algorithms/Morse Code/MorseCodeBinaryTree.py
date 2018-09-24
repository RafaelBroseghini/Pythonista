'''
Name: Rafael Broseghini
Prof: Roman Yasinovskyy

Filename: MorseCodeBinaryTree.py
Date: 04/25/2017
'''
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def height(self):
        if self.key == None:
            return 0
        return max(self.leftChild.height() if self.leftChild is not None else 0, self.rightChild.height() if self.rightChild is not None else 0) + 1    


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key 
    
    def __str__(self):
        return str(self.key)



def MorseTree():
    Tree = BinaryTree('')
    with open('morse.txt') as file:
        mydict = dict()
        for line in file:
            (key, val) = line.split()
            mydict[key] = val
            cur = Tree
            for dash_or_dot in val:
                if dash_or_dot == '.':
                    if cur.getLeftChild() == None:
                        cur.insertLeft('')
                    cur = cur.getLeftChild()
                elif dash_or_dot == '-':
                    if cur.getRightChild() == None:
                        cur.insertRight('')
                    cur = cur.getRightChild()
            cur.setRootVal(key)
        return Tree
    
def decode(message: str) -> list:
    x = message.split(' ')
    mylist = []
    for letter in x:
        cur = MorseTree()
        for i in letter:
            if i == '.':
                cur = cur.getLeftChild()
            elif i == '-':
                cur = cur.getRightChild()           
        mylist.append(str(cur))
    newlist = ','.join(mylist)
    newlist = newlist.replace(',','')
    return newlist

def encode(message: str) -> str:
    output = ''
    message = message.split(' ')
    for word in message:
        for letter in word:
            output = output + findpath(MorseTree(), letter, '') + ' '
    return output
        
        
        
def findpath(mytree: MorseTree, letter: str, path: str) -> str:
    if not mytree:
        return False
    elif mytree.getRootVal() == letter:
        return path
    else:
        return findpath(mytree.getLeftChild(), letter, path + '.') or findpath(mytree.getRightChild(), letter, path + '-')
    
    


def main():
    print()
    print("Let's take a look at a Morse Code Binary Tree!")
    print()
    r = MorseTree()
    print('The right child of the root of the MorseTree is:', r.getRightChild())
    print()
    print('The left child of the root of the MorseTree is:', r.getLeftChild())
    print()
    print('The right child of', r.getRightChild(), 'is:', r.getRightChild().getRightChild())
    print()
    print('The left child of', r.getLeftChild(), 'is:', r.getLeftChild().getLeftChild())
    print()
    print('The height of the entire MorseTree is:', r.height())
    print()
    print('My message in morse code to you is:', decode('--. .. ...- . ..--.- -- . ..--.- .- -. ..--.- .- ..--.- ..-. --- .-. ..--.- - .... .. ... ..--.- -.-. .-.. .- ... ...'))
    print()
    print('Translating "rafael" to morse code:', encode('rafael'))
main()

