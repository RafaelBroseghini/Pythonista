NoTransition = -1
    
class State:
    def __init__(self, id, acceptsTokenId = None, transitions = []):
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
        self.transitions = list(transitions)
        self.acceptsTokenId = acceptsTokenId
        
        # This will cause onGoTo to generate an Exception if called
        # before the setClasses method is called. 
        self.classes = None 
        
    def setClasses(self, classes):
        self.classes = classes      
        
    def addTransition(self, onClass, toState):
        self.transitions.append((onClass, toState))
        
    def hasTransition(self, onClass):
        for aClass, toStateId in self.transitions:
            if onClass == aClass:
                return True
            
        return False
    
    def onClassGoTo(self, onClass):
        for aClass, toStateId in self.transitions:
            if onClass == aClass:
                return toStateId
            
        return NoTransition
    
    # You must call setClasses before calling the onGoTo method.
    def onGoTo(self, on):
        for aClass, toStateId in self.transitions:
            if on in self.classes[aClass]:
                return toStateId
            
        return NoTransition       
                  
    def getTransitions(self):
        return self.transitions

    def getId(self):
        return self.id
    
    def setAccepting(self, tokenId):
        self.acceptsTokenId = tokenId
        
    def isAccepting(self):
        return self.acceptsTokenId != None
    
    def getAcceptsTokenId(self):
        return self.acceptsTokenId
    
    def __repr__(self):
        return "State(" + repr(self.id) + "," + repr(self.acceptsTokenId) + "," + \
            repr(self.transitions) + ")"
    
    def __str__(self):
        val = ""
        val = "State " + str(self.id) + "\n" 
        if self.acceptsTokenId != None:
            val += "    accepts token with identifier: " + str(self.acceptsTokenId) + "\n"
            
        for on, toStateId in self.transitions:
            val += "    On " + str(on) + " Go To " + str(toStateId) + "\n"
            
        return val
