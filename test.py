import random

class Die(object):

    def __init__ (self, face =None, faceValue = None):
        self.face = face
        self.faceValue = faceValue
    def roll(self):
            self.faceValue = random.randint(1, 6)
            if self.faceValue == 1:
                self.face = (
                    ' ------\n'
                    '|      |\n'
                    '|   o  |\n'
                    '|      |\n'
                    ' ------')
            elif self.faceValue == 2:
                self.face = (
                    ' ------\n'
                    '| o    |\n'
                    '|      |\n'
                    '|    o |\n'
                    ' ------')
            elif self.faceValue == 3:
                self.face = (
                    ' ------\n'
                    '| o    |\n'
                    '|   o  |\n'
                    '|     o|\n'
                    ' ------')
            elif self.faceValue == 4:
                self.face = (
                    ' ------\n'
                    '| o   o|\n'
                    '|      |\n'
                    '| o   o|\n'
                    ' ------')
            elif self.faceValue == 5:
                self.face = (
                    ' ------\n'
                    '| o   o|\n'
                    '|   o  |\n'
                    '| o   o|\n'
                    ' ------')
            elif self.faceValue == 6:
                self.face = (
                    ' ------\n'
                    '| o   o|\n'
                    '| o   o|\n'
                    '| o   o|\n'
                    ' ------')
    def __str__(self):
            return str(self.face)
class DiceGame(Die):
    def play(self):
        self.roll()
        return self.face

go = DiceGame()
print(go.play())