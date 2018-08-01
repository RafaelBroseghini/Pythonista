from genscanner import *
from state import *

#TOKEN Constants
TokenToIDMap = {'number':0,'(':1,')':2,'+':3,'-':4,'*':5,'/':6,'S':7,'R':8,';':9,'endoffile':10}
IDToTokenMap = {0:'number',1:'(',2:')',3:'+',4:'-',5:'*',6:'/',7:'S',8:'R',9:';',10:'endoffile'}

#KEYWORD Constants

class calcScanner(Scanner):
	def __init__(self,instream):
		super().__init__(instream,0,{0: State(0,None,[('(', 1), (')', 2), ('*', 3), ('+', 4), ('-', 5), ('/', 6), (';', 7), ('EOF', 8), ('R', 9), ('S', 10), ('digit', 11)]), 1: State(1,1,[]), 2: State(2,2,[]), 3: State(3,5,[]), 4: State(4,3,[]), 5: State(5,4,[]), 6: State(6,6,[]), 7: State(7,9,[]), 8: State(8,10,[]), 9: State(9,8,[]), 10: State(10,7,[]), 11: State(11,0,[('digit', 11), ('period', 12)]), 12: State(12,None,[('digit', 13)]), 13: State(13,0,[('digit', 13)])},{'(': OrderedSet({40}), 'digit': OrderedSet({48, 49, 50, 51, 52, 53, 54, 55, 56, 57}), 'S': OrderedSet({83}), 'EOF': OrderedSet({3}), 'period': OrderedSet({46}), '+': OrderedSet({43}), '-': OrderedSet({45}), 'EPSILON': OrderedSet(), '/': OrderedSet({47}), 'R': OrderedSet({82}), '*': OrderedSet({42}), ';': OrderedSet({59}), ')': OrderedSet({41})},{},0,False)

