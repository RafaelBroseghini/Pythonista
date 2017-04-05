import random
class Card:
    def __init__(self, rank, suit):
        if rank in '23456789TJQKA':
            self._rank = rank
        else:
            raise ValueError('Invalid rank')
        if suit in ['spades','clubs','diamonds','hearts']:
            self._suit = suit
        else:
            raise ValueError('Invalid suit')
        
    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __gt__(self, other):
        if self._suit == other._suit:
            return '23456789TJQKA'.index(self._rank) > '23456789TJQKA'.index(other._rank)
        if self._rank == other._rank:
            return ['spades','clubs','diamonds','hearts'].index(self._suit) > ['spades','clubs','diamonds','hearts'].index(self._suit) 
        
    def __lt__(self, other):
        card1 = self._suit, self._rank
        card2 = other._suit, other._rank
        return card1 < card2      
    
    def __eq__(self, other):
        if isinstance(other, Card):
            if self._rank == other._rank and self._suit == other._suit:
                return True
            else:
                return False
    
    def __str__(self):
            return str(self._rank) + ' of ' + str(self._suit)
        
        
print('1.')       
def sequentialSearch(alist, item):
    pos = 0
    found = False
        	
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
        	
    return found
        	
testlist = [Card('3', 'clubs'), Card('8', 'clubs'),Card('A', 'clubs'),Card('2', 'spades'), Card('2', 'diamonds'), Card('2', 'hearts'), Card('K', 'diamonds'), Card('9', 'hearts'), Card('8', 'diamonds'), Card('T', 'spades')]
print(sequentialSearch(testlist, Card('K', 'diamonds')))
print(sequentialSearch(testlist, Card('8', 'clubs')))

print()
print('2.')  
def binarySearch(lst, item):
    first = 0
    last = len(lst)-1
    found = False
	
    while first <= last and not found:
        midpoint = (first + last)//2
        if lst[midpoint] == item:
            found = True
        else:
            if item > lst[midpoint]:
                first = midpoint+1
            else:
                last = midpoint-1
                
    return found     
	
mytestlist = ['Rafa', 'Mosley', 'Erick', 'Bob', 'Holly', 'Hank', 'Brit', 'Carlos', 'Antony']

print(binarySearch(sorted(mytestlist), 'Rafa'))







# Hash Function using simple remainder method.

table = [0] * 11

def hash_function(x): 
    return x % 11

def insert(table,input,value): 
    table[hash_function(input)] = value



def main():
    print()
    print()
    print()
    print('3.')       
    for i in range(11):
        x = random.randint(100, 999)
        print('New Random generated number is:', x)
        print('Random number ' + str(x) + ' goes in slot ' + str(x%11) + ' using simple remainder method.')
        print()
        insert(table,x,x)
    print('Table result using simple remainder method:', table)
main()

#---------------------------------------------#


# Hash Function using mid square method.
print()
mytable = [0] * 11
print()
print()
print()
print('4.')      
for i in range(11):
    x = random.randint(100, 999)
    print('New Random generated number is:', x)
    a = str(x * x)
    print('Random number squared result:', a)
    b = a[2:4]
    print('Mid Square point (2 digits):', b)
    c = int(b) % 11
    print('Random number ' + str(x) + ' goes in slot number: ' + str(c))
    print()
    insert(mytable,c,x)
print('Table result using mid square point method:', mytable)

#--------------------------------------------------------------------------#


# Hash Function cat weight.

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])*(pos+1)

    return sum%tablesize

def main():
    tablesize = [0] * 11
    print()
    print()
    print()
    print()
    print('5.') 
    print("The string 'cat' goes in slot:", hash('cat', 11))
    print()
    insert(tablesize,hash('cat', 11), 'cat')
    print("The string 'algorithm' goes in slot:", hash('algorithm', 11))   
    print()
    insert(tablesize,hash('algorithm', 11), 'algorithm')
    print("The string 'logarithm' goes in slot:", hash('logarithm', 11))    
    print()
    insert(tablesize,hash('logarithm', 11), 'logarithm')
    print('Table result using hash function with weight:', tablesize)
main()
