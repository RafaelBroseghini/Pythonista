'''
Name: Rafael Lopes Broseghini
Purpose: Create Turing machine that reverses a string of any amount of'r','e','v',s'
'''

import unittest

class TuringMachine:
    def __init__(self,startState = 0, delta = {}, finalStates = set()):
        self.startState = startState
        self.delta = delta
        self.finalStates = finalStates
        
        
    def run_machine(self, inputString: str) -> str:
        
        tape = Tape(inputString)
        
        theState = self.startState
        
        startRead = tape.read()   
        
        key = (theState, startRead)
        
        reached_final = False
        transition_num = 0
        
        while key in self.delta and not reached_final:
            
            # Keeping track of how many transitions.
            transition_num += 1
            
            #Storing what state it goes to, what to write on the tape, what direction to move.
            goTo, writeToTape, moveDirection = self.delta[key]
                    
                
            # print('Transition num:', transition_num,'Read:',tape.read(),'Going to state:',goTo,'Writing:',writeToTape,'Read at position:',tape.tapeReadPos, 'Moving to the:',moveDirection)
            # print()
            
            # Writing to the tape.
            tape.write(writeToTape)
            
            if moveDirection == 'R':
                tape.move_right()
                # Set new key to state it went to and the input symbol after having moved right.
                key = (goTo,tape.read())
            elif moveDirection == 'L':   
                tape.move_left()
                # Set new key to state it went to and the input symbol after having moved left.
                key = (goTo,tape.read())
            else:
                tape.not_move()
                # Set new key to state it went to and the input symbol after having not moved left.
                key = (goTo,tape.read())
                
            # If reached final state.
            if goTo in self.finalStates:
                # have to fix this because I want to just return the tape and not 
                # mess with the tape object from the turing machine object.
                tape = ''.join(tape.contents).strip()
                return '|{}|'.format('|'.join(list(tape)))
                reached_final = True
        
class Tape:
    
    def __init__(self, inputRead = ''):
        self.contents = [' ' for item in range(50)]+list(inputRead)+[' ' for item in range(50)]
        self.tapeReadPos = 50
        
    def read(self) -> str:
        return self.contents[self.tapeReadPos]
    
    def write(self, ch: str) -> str:
        self.contents[self.tapeReadPos] = ch
        
    def move_right(self) -> None:
        self.tapeReadPos += 1
        if self.tapeReadPos == len(self.contents):
            for item in range(len(self.contents)):
                self.contents.append(' ')
                
    def move_left(self) -> None:
        self.tapeReadPos -= 1
        if self.tapeReadPos == -1:
            self.contents =  [' ' for item in range(len(self.contents))] + self.contents 
            self.tapeReadPos = len(self.contents)//2 - 1
    
    # Not move. Only accessed when reaches a final state.
    def not_move(self) -> None:
        self.tapeReadPos = self.tapeReadPos
           
        
    def __str__(self) -> str:
        tape = ''.join(self.contents).strip()
        return '|{}|'.format('|'.join(list(tape)))



class TestTuringMachine(unittest.TestCase):
    
    def test(self):
        delta = {(0,'$') : (1,'$','R'),(1,'x'):(1,'x','R'),(1,'r'):(2,'x','L'),(1,'e'):(5,'x','L'),(1,'v'):(4,'x','L'),(1,'s'):(3,'x','L'),(1,'$'):(10,' ','L'),(2,'$'):(2,'$','L'),(2,'x'):(2,'x','L'),(2,'r'):(2,'r','L'),(2,'e'):(2,'e','L'),(2,'v'):(2,'v','L'),(2,'s'):(2,'s','L'),(2,'e'):(2,'e','L'),(2,' '):(6,'r','R'),(3,'$'):(3,'$','L'),(3,'r'):(3,'r','L'),(3,'e'):(3,'e','L'),(3,'v'):(3,'v','L'),(3,'s'):(3,'s','L'),(3,'x'):(3,'x','L'),(3,' '):(7,'s','R'),(4,'$'):(4,'$','L'),(4,'r'):(4,'r','L'),(4,'e'):(4,'e','L'),(4,'v'):(4,'v','L'),(4,'s'):(4,'s','L'),(4,'x'):(4,'x','L'),(4,' '):(8,'v','R'),(5,'$'):(5,'$','L'),(5,'r'):(5,'r','L'),(5,'e'):(5,'e','L'),(5,'v'):(5,'v','L'),(5,'s'):(5,'s','L'),(5,'x'):(5,'x','L'),(5,' '):(9,'e','R'),(6,'r'):(6,'r','R'),(6,'e'):(6,'e','R'),(6,'s'):(6,'s','R'),(6,'v'):(6,'v','R'),(6,'$'):(1,'$','R'),(7,'r'):(7,'r','R'),(7,'e'):(7,'e','R'),(7,'s'):(7,'s','R'),(7,'v'):(7,'v','R'),(7,'$'):(1,'$','R'),(8,'r'):(8,'r','R'),(8,'e'):(8,'e','R'),(8,'s'):(7,'s','R'),(8,'v'):(8,'v','R'),(8,'$'):(1,'$','R'),(9,'r'):(9,'r','R'),(9,'e'):(9,'e','R'),(9,'s'):(9,'s','R'),(9,'v'):(9,'v','R'),(9,'$'):(1,'$','R'),(10,'$'):(11,'$','L'),(10,'x'):(10,' ','L'),(11,'r'):(11,'r','L'),(11,'e'):(11,'e','L'),(11,'s'):(11,'s','L'),(11,'v'):(11,'v','L'),(11,' '):(12,'$','N')}
        # Set final state.
        finalStates = set([12])
        tm = TuringMachine(0, delta, finalStates)
        tape = Tape()
        self.assertEqual(tm.run_machine('$reverse$'), "|$|e|s|r|e|v|e|r|$|")

if __name__ == "__main__":
    unittest.main()
    # main()

