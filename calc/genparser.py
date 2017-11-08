from lr0state import *
import stack
import streamreader
import io
import sys

class Parser:
    def __init__(self,states,tnts):
        self.states = states
        self.tnts = tnts
        for stateId in states:
            theState = states[stateId]
            theState.tnts = tnts
            for item in theState.items:
                item.tnts = tnts


    def buildReturnValue(self,item,prodStack):
        # We found an item to reduce by.
        prodNames = {} # this is a map from return value names to locations with rhs
        tntCount = {}
        rhsVals = {} # this is a map from index location of rhs to value from the stack.

        # this loop builds a map from names of rhs terminals or nonterminals to
        # their index value for the rhs
        for i in range(len(item.production.rhs)):
            tntId = item.production.rhs[i]
            tnt = self.tnts[tntId]
            if not tnt in tntCount:
                tntCount[tnt] = 1
                prodNames[tnt] = i
                prodNames[tnt+"1"] = i
            else:
                numVal = tntCount[tnt]+1
                tntCount[tnt] = numVal
                prodNames[tnt+str(numVal)]=i


        # this loop builds a map from index value of rhs location to
        # the actual value popped from the pda stack.
        for i in range(len(item.production.rhs)-1,-1,-1):
            stateId, val = prodStack.pop()
            rhsVals[i] = val

        returnValue = ""
        rvStrm  = streamreader.StreamReader(io.StringIO(item.production.returnValue))

        # Here we iterate through the parts of the return value replacing any
        # non-terminal token with the actual value popped from the stack
        # used in parsing. This builds the actual return value for the expression
        # being parsed.

        token = rvStrm.getToken()

        while not rvStrm.eof():
            if token in prodNames:
                returnValue += rhsVals[prodNames[token]]
            else:
                returnValue += token

            token = rvStrm.getToken()

        # Here we call the overridden eval method to evaluate
        # the return value string in the context of the parser's
        # back end module. This is because each parser instance
        # inherits from this class to define its own parser
        # and backend code.

        val = repr(self.eval(returnValue))
        return val

    # This is called in case of an error because no shift or reduce was possible.
    def error(self,stateId,tokenId,prodStack,lex):
        sys.stderr.write("No Transition Found\n")
        sys.stderr.write("\nState is " + str(stateId) + "\n\n")
        sys.stderr.write("Stack Contents\n")
        sys.stderr.write("==============\n\n")
        sys.stderr.write(str(prodStack)+"\n\n\n")
        sys.stderr.write("Next Input Symbol is " +lex+ " with tokenId of "+str(tokenId)+"\n\n")
        raise Exception("No transition on state!")


    # This algorithm comes from page 218, Algorithm 4.7 from Aho,
    # Sethi, and Ullman.
    # The modification from this algorithm has the stack a stack of
    # tuples of (stateId, val) where val is the return value
    # for a terminal or nonterminal.
    
    def parse(self, theScanner):

        # create a stack called prodStack.
        prodStack = stack.Stack()
        
        # push the start state and return value. The initial return value can be None.
        prodStack.push((0, None))

        need_token = True
        while True:
            
            # Peek at the top of the stack to get the stateId and return value.
            stateId, value = prodStack.peek()
            
            theState = self.states[stateId]
            
            if theState.isAccepting():
                return value            
            
            # Get a token if needed.
            if need_token:
                tokenId, lex = theScanner.getToken()
                need_token = False
            
            # Do a shift operation if there is a transition on the tokenId. If we also had the same
            # tokenId in a lookahead set we would have a shift/reduce conflict, but we'll always shift
            # anyway in that case so don't worry about detecting shift/reduce conflicts.

            if theState.hasTransition(tokenId):
                print(tokenId, lex)
                #This is a shift operation.
                prodStack.push((theState.onClassGoTo(tokenId), lex))
                need_token = True
                
            
            # If no shift operation is possible then look for a reduce possibility.
            # we look in the items of the state for an item that would
            # work to reduce by. If more than one item is found then we have a
            # reduce/reduce conflict.
            
            else:
                reduced = False
                for item in theState.items:
                    prod = item.production
                    if tokenId in item.la:         #and item.dotIndex == len(prod.rhs):
                        
                        #Reduce operation.
                        if reduced:
                            self.error(stateId,tokenId, prodStack,lex)
                            
                        # If an item to reduce by is found then call buildReturnValue which will build the return
                        # value (e.g. usually an AST) for the reduction.
                        
                        val = self.buildReturnValue(item, prodStack)
                        
                        # NOTE: buildReturnValue pops off the correct number of values from the stack, but does not
                        # push on the new state found by following the transition on the LHS of the chosen item.                        
                        
                        stateId, value = prodStack.peek()
                        prodStack.push((self.states[stateId].onClassGoTo(prod.lhsId), val))
                        reduced = True
                        
                        
                # if no item was found for a shift or reduce operation, then tere is a problem so raise an exception
                # by calling the error function.
                if not reduced:
                    self.error(stateId,tokenId,prodStack,lex)
                    
        