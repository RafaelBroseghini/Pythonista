epsilon = "EPSILON" 
NoTransition = -1

class LR0State:
    def __init__(self, id, items = frozenset(), transitions = {}, accepting = False):
        # An id of -1 is not allowed since that indicates there is 
        # no transition on a value.
        if id == -1:
            raise Exception("A state id of -1 is not allowed.")
        
        self.id = id
        # A copy of the list of transitions needs to be created
        # because Python makes only one instance of a default
        # parameter. Changing the list later, by adding a transition
        # would add that transition to every state. Wow! Talk about
        # bad semantics...
        self.transitions = dict(transitions)
        self.predecessors = dict()
        self.items = items
        self.accepting = accepting
        self.tnts = None
        
    def __hash__(self):
        val = 0
        for item in self.items:
            val = (val + hash(item)) % 999999999
        
        return val
    
    def __eq__(self,other):
        if len(self.items) != len(other.items):
            return False
        
        for item in self.items:
            if not item in other.items:
                return False
            
        return True
    
    def isAccepting(self):
        return self.accepting
    
    def setClasses(self, classes):
        self.classes = classes      
        
    def addTransition(self, onClass, aState):
        self.transitions[onClass]=aState.id
        if onClass in aState.predecessors:
            aState.predecessors[onClass].add(self.id)
        else:
            aState.predecessors[onClass] = set([self.id])
        
    def hasTransition(self, onClass):
        return onClass in self.transitions
    
    def onClassGoTo(self, onClass):
        if onClass in self.transitions:
            return self.transitions[onClass]
            
        return NoTransition
              
    def pred(self, onClass):
        if onClass in self.predecessors:
            return self.predecessors[onClass]
        
        return -1
        
    def getTransitions(self):
        return self.transitions

    def getId(self):
        return self.id
    
    #def productions(self):
    #    prodSet = set()
    #    for item in self.items:
    #        prodSet.add(item.production.id)
    #        
    #    return prodSet
              
    def __repr__(self):
        return "LR0State(" + repr(self.id) + "," + repr(self.items) + "," + \
            repr(self.transitions) + "," + repr(self.accepting) + ")"
    
    def __str__(self):
        val = ""
        val = "LR0State " + str(self.id) 
        if self.accepting:
            val += " is accepting\n"
        else:
            val += "\n"
            
        for on in self.transitions:
            toStateId = self.transitions[on]
            val += "    On " + str(self.tnts[on]) + " Go To " + str(toStateId) + "\n"
            
        for item in self.items:
            val += "    Item: " + str(item) + "\n"        
            
        return val

class Production:
    def __init__(self, id, lhsId = None, rhs = [], returnValue = ""):
        self.id = id
        self.rhs = list(rhs)
        self.lhsId = lhsId
        self.returnValue = returnValue
        self.tnts = None


    def addRHSItem(self, tntId):
        self.rhs.append(tntId)
        
    def __str__(self):
        if self.tnts != None:
            s = self.tnts[self.lhsId] + " --> "
            for k in range(len(self.rhs)):   
                s += self.tnts[self.rhs[k]] + " "
                             
            return s
        
        return repr(self)
    
    def __repr__(self):
        return "Production(" + repr(self.id) + "," + repr(self.lhsId) + "," + repr(self.rhs) + "," + repr(self.returnValue) + ")"

class LR0Item:
    def __init__(self,id,production=None,dotIndex=0,la=frozenset()):
        # make a copy of the set and list below
        # because sets are mutable and
        # default arguments are only created once.
        self.id = id
        self.production = production
        self.dotIndex = dotIndex
        self.tnts = None
        self.la = set(la)
        
    def __eq__(self,other):
        if type(self)!=type(other):
            raise Exception("Comparison of LR0Item " + str(self) + " with " + str(other))
        
        return self.dotIndex == other.dotIndex and self.production.id == other.production.id
    
    def __hash__(self):
        # the 100000 is really just a random number, but it
        # does allow for a unique hash code up to 100,000 elements
        # (i.e. terminal and nonterminals) on the right hand
        # side of any production.
        return self.production.id * 100000 + self.dotIndex
    
    def __str__(self):
        if self.tnts != None:
            s = self.tnts[self.production.lhsId] + " ::= "
            if len(self.production.rhs) == 0:
                s += "(*)"
            else:
                for k in range(len(self.production.rhs)):
                    if k == self.dotIndex:
                        s += "(*) "
                        
                    s += self.tnts[self.production.rhs[k]] + " "
                    
                if self.dotIndex == len(self.production.rhs):
                    s += "(*)"
                    
            if len(self.la) != 0:
                s+= "\n        Lookaheads: "
                first = True
                for termId in self.la:
                    if first:
                        first = False
                    else:
                        s+=", "
                    s+= self.tnts[termId]
            s+="\n"
            return s
        
        return repr(self)
    
    def __repr__(self):
        return "LR0Item(" + repr(self.id) + "," + repr(self.production) + "," + repr(self.dotIndex) + "," + repr(self.la) + ")" 
    
    
