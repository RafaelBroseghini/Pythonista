"""
Name: Rafael Broseghini
Date: 10/23/2017


Course: CS 260
Prof: Dr. Kent Lee
"""


import sys
import stack
import nfastate
import streamreader
import orderedcollections

epsilon = "EPSILON"

##########################################################################
# You should use the Operator class in your code for each of the regular
# expression operators. The precedence function will give you the
# precedence of each regular expression operator.
##########################################################################


class Operator:
    def __init__(self, op):
        self.op = op

    def precedence(self):
        if self.op == "|":
            return 1
        if self.op == ".":
            return 2
        if self.op == "*":
            return 3
        if self.op == "(" or self.op == ")":
            return 0

    def getOpChar(self):
        return self.op


class NFA:
    def __init__(
        self,
        classes={epsilon: orderedcollections.OrderedSet()},
        states=orderedcollections.OrderedMap(),
        keywords=orderedcollections.OrderedMap(),
        tokens=orderedcollections.OrderedMap(),
        firstTokenId=-1,
    ):
        self.classes = orderedcollections.OrderedMap(classes)
        self.states = orderedcollections.OrderedMap(states)
        self.numStates = len(states)
        self.keywords = orderedcollections.OrderedMap(keywords)
        self.tokens = orderedcollections.OrderedMap(tokens)
        self.firstTokenId = firstTokenId

    def __repr__(self):
        return (
            "NFA("
            + repr(self.classes)
            + ","
            + repr(self.states)
            + ","
            + repr(self.keywords)
            + ","
            + repr(self.tokens)
            + ","
            + repr(self.firstTokenId)
            + ")"
        )

    def getFirstTokenId(self):
        return self.firstTokenId

    def buildMachine(self, instream):

        #######################################################################
        # The newState function should be called to create any new state. It enters
        # the state information into the self.states dictionary for use later. Then
        # it returns the state Id (its state number) of the newly created state.
        #######################################################################

        def newState():
            self.numStates += 1
            aState = nfastate.NFAState(self.numStates)
            self.states[self.numStates] = aState
            return self.numStates

        #######################################################################
        # The operate function is given an:
        #   op : the operator
        #
        #   opStack: the stack of operators
        #
        #   stateStack: the stack of first,last states (which is the operand stack)
        #   the function does not return anything. Instead it operates on the two
        #   stacks as described in the two stack calculator algorithm.
        #
        # For each new state be sure to call the newState() function to enter
        # the new state in the self.states dictionary correctly.
        #######################################################################

        def operate(op, opStack, stateStack):
            precedence = {"(": 0, "|": 1, ".": 2, "*": 3, ")": 0}

            if op == "(":
                opStack.push(op)
                return None
            else:
                topOp = opStack.pop()
                opStack.push(topOp)
                while precedence[op] <= precedence[topOp]:
                    topOp = opStack.pop()
                    if topOp == ".":
                        first_operand = stateStack.pop()
                        second_operand = stackStack.pop()

                        startStateID = newState()
                        finalStateId = newState()
                        startState = self.states[startStateID]
                        finalState = self.states[finalStateId]
                        finalState.setAccepting(self.numStates)

                        q0 = self.states[first_operand]
                        q1 = self.states[second_operand]

                        q0.addTransition(epsilon, q1)
                        startState.addTransition(epsilon, q0)
                        q1.addTransition(epsilon, finalState)
                    elif topOp == "|":
                        first_operand = stateStack.pop()
                        second_operand = stackStack.pop()
                        operandNum3 = stateStack.pop()
                        operandNum4 = stackStack.pop()

                        startStateID = newState()
                        finalStateId = newState()
                        startState = self.states[startStateID]
                        finalState = self.states[finalStateId]
                        finalState.setAccepting(self.numStates)

                        q0 = self.states[first_operand]
                        q1 = self.states[second_operand]
                        q2 = self.states[operandNum3]
                        q3 = self.states[operandNum4]

                        q0.addTransition(epsilon, q1)
                        q1.addTransition(epsilon, finalState)
                        q2.addTransition(epsilon, q3)
                        q3.addTransition(epsilon, finalState)
                        startState.addTransition(epsilon, q0)
                        finalState.addTransition(epsilon, q2)

                        stateStack.push((startStateID, finalStateId))

                        stateStack.push((startStateID, finalStateId))
                    elif topOp == "*":
                        first_operand = stateStack.pop()
                        second_operand = stackStack.pop()

                        startStateID = newState()
                        finalStateId = newState()
                        startState = self.states[startStateID]
                        finalState = self.states[finalStateId]
                        finalState.setAccepting(self.numStates)

                        q0 = self.states[first_operand]
                        q1 = self.states[second_operand]

                        q0.addTransition(epsilon, q1)
                        startState.addTransition(epsilon, q0)
                        startState.addTransition(epsilon, q1)
                        q1.addTransition(epsilon, finalState)
                        finalState.addTransition(epsilon, startState)

                        stateStack.push((startStateID, finalStateId))
                    elif topOp == "(":
                        return None

                opStack.push(op)

        #######################################################################
        # The evaluateRegExpression function is given the StreamReader called
        # reader and reads the regular expression and returns a tuple of start,stop state
        # for the expression. The stop state will be set to an accepting state by the code
        # that calls this function. When this function is called the regular expression must be
        # read. For instance in the line
        #
        # identifier = letter.(letter|digit)*;
        #
        # everything up to the = has already been read. You need to write code to read the
        # regular expression up to the semicolon (i.e. ;) and then run your regular expression
        # calculator code on it to build an NFA from this. To create each new state be sure to call
        # the newState() function to create it so the state gets entered into the self.states dictionary
        # correctly.
        #######################################################################

        def evaluateRegExpression(reader):
            opStack = stack.Stack()
            opdStck = stack.Stack()
            opStack.push("(")

            operand_classes = {"(", "|", ".", "*", ")"}
            precedence = {"(": 0, "|": 1, ".": 2, "*": 3, ")": 0}

            while not reader.peek(";"):
                if reader.peek("(" or "|" or "." or "*" or ")"):
                    token = reader.getToken()
                    operate(token, opStack, opdStck)
                else:
                    startStateID = newState()
                    finalStateId = newState()
                    startState = self.states[startStateID]
                    finalState = self.states[finalStateId]

                    token = reader.getToken()
                    startState.addTransition(token, finalState)
                    opdStck.push(startStateID)
                    opdStck.push(finalStateId)
            operate(")", opStack, opdStck)
            return startStateID, finalStateId

        ####################################################
        # This is the start of the buildMachine code here
        ####################################################

        reader = streamreader.StreamReader(instream)
        startStates = []

        reader.skipComments()

        if reader.peek("#CLASSES"):
            # print("Found #CLASSES")
            reader.readUpTo("\n")
            while not reader.peek("#"):
                # The "#" marks the beginning of the next section. Either KEYWORDS or TOKENS. KEYWORDS are optional.
                reader.skipComments()

                # We could have keywords right after a comment. So if keyword section is found, don't read
                # any more character classes.
                if not reader.peek("#KEYWORDS"):
                    className = reader.readIdentifier()
                    reader.readUpTo("=")
                    if reader.peek("^"):
                        rev_class = True
                        reader.readUpTo("^")
                        classSet = orderedcollections.OrderedSet(range(256))
                    else:
                        rev_class = False
                        classSet = orderedcollections.OrderedSet()

                    done = False

                    while not done:

                        if reader.peek("'"):
                            # Found a character constant
                            reader.readUpTo("'")
                            character = reader.readUpTo("'")[0]
                            # print(character)
                            value = ord(character)

                        else:
                            value = reader.readInt()

                        # Add the end of the range if there is a range of characters
                        if reader.peek(".."):
                            reader.readUpTo("..")

                            if reader.peek("'"):
                                reader.readUpTo("'")
                                character = reader.readUpTo("'")[0]
                                # print(character)
                                lastValue = ord(character)
                            else:
                                lastValue = reader.readInt()
                        else:
                            lastValue = value

                        # Now build the set
                        for i in range(value, lastValue + 1):
                            if rev_class:
                                classSet.remove(i)
                            else:
                                classSet.add(i)

                        if reader.peek(","):
                            reader.readUpTo(",")
                        else:
                            done = True

                    # print(className)
                    # Add the class to the class dictionary

                    self.classes[className] = classSet

                    reader.readUpTo(";")

        # print("These are the classes")
        # print(self.classes)
        # keyword and token id numbers
        IdNum = 0
        keywordsPresent = False

        if reader.peek("#KEYWORDS"):
            reader.readUpTo("#KEYWORDS")
            keywordsPresent = True
            reader.skipComments()
            while not reader.peek("#TOKENS"):
                # IdNum = reader.readInt()
                # reader.readUpTo(":")
                reader.readUpTo("'")
                keyword = reader.readUpTo("'")[:-1].strip()
                # print(IdNum,keyword)
                self.keywords[keyword] = IdNum
                IdNum += 1
                reader.readUpTo(";")
                reader.skipComments()
        reader.readUpTo("#TOKENS")
        reader.skipComments()
        readingFirstToken = True

        while not (
            reader.peek("#PRODUCTIONS")
            or reader.peek("#END")
            or reader.peek("#DEFINITIONS")
        ):
            # idnum = reader.readInt()
            # reader.readUpTo(":")
            if reader.peek("'"):
                # Then the token was specified as a string like this:
                # '>=';
                reader.readUpTo("'")
                token = reader.readUpTo("'")[:-1].strip()
                previousId = newState()
                startStateId = previousId

                for c in token:
                    nextId = newState()
                    classSet = orderedcollections.OrderedSet([ord(c)])
                    if not (c in self.classes and self.classes[c] == classSet):
                        self.classes[c] = classSet
                    self.states[previousId].addTransition(c, nextId)
                    previousId = nextId

                self.states[nextId].setAccepting(IdNum)
                startStates.append(startStateId)
                reader.readUpTo(";")
                self.tokens[IdNum] = token
                IdNum += 1
                if readingFirstToken and keywordsPresent:
                    raise Exception(
                        "First Token must be identifier token for matching keywords!"
                    )

            else:
                # The token was specified as a regular expression like this:
                # identifier = letter.(letter|digit)*;

                name = reader.readUpTo("=")[:-1].strip()
                self.tokens[IdNum] = name
                if readingFirstToken:
                    self.firstTokenId = IdNum
                    readingFirstToken = False

                # You must write the evaluateRegExpression(reader) function
                # that reads a regular expression using the reader StreamReader
                # object and returns its start and stop state ids.
                startStateId, stopStateId = evaluateRegExpression(reader)

                self.states[stopStateId].setAccepting(IdNum)
                IdNum += 1
                startStates.append(startStateId)

                reader.readUpTo(";")
                reader.skipComments()

        # Create a 0th State as the start state
        startState = nfastate.NFAState(0)
        self.numStates += 1
        self.states[0] = startState

        for startId in startStates:
            self.states[0].addTransition(epsilon, startId)

        self.startStateId = 0

        reader.readUpTo("#END")

    def writeListing(self, outStream):

        outStream.write("The NFA CREATED FOR THE REGULAR EXPRESSIONS IS:\n\n")

        outStream.write("The start state is: " + str(self.startStateId) + "\n\n")

        outStream.write("STATE           ON CLASS         GO TO     ACCEPTS\n")
        outStream.write("-----           --------         -----     -------\n")

        for stateId in range(self.numStates):
            if self.states[stateId].isAccepting():
                acceptsId = self.states[stateId].getAcceptsTokenId()
                tokenName = self.tokens[acceptsId]
            else:
                tokenName = ""

            outStream.write("%5d %44s\n" % (stateId, tokenName))

            trans = self.states[stateId].getTransitions()

            for onClass in trans:
                toStateIds = trans[onClass]
                for toStateId in toStateIds:
                    # Fix this error!!

                    # outStream.write("%28s     %5d\n" % (onClass, toStateId))

                    outStream.write("\n")


def main():

    filename = "jpython.txt"

    instream = open(filename, "r")

    nfa = NFA()
    nfa.buildMachine(instream)
    nfa.writeListing(sys.stdout)


if __name__ == "__main__":
    main()
