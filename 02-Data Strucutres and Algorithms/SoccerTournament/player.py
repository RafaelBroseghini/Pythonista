import random
class Player():
    def __init__(self, number, name, lastname, position, height, weight, grade, town, highschool,score=0):
        self._number = number
        self._name = name
        self._lastname = lastname
        self._position = position
        self._height = height
        self._weight = weight
        self._grade = grade
        self._town = town
        self._highschool = highschool
        self._score = score

        if self._grade == 'Sr':
            self._score += 4.25
        elif self._grade == 'Jr':
            self._score += 3.90
        elif self._grade == 'So':
            self._score += 3.70
        else:
            self._score += 3.45
        
        if self._position == "Midfielder":
            self._score += random.randint(3, 5) + round(random.random(),2)
        elif self._position == 'Forward':
            self._score += random.randint(4,5) + round(random.random(),2)
        else:
            self._score += random.randint(2,4) + round(random.random(),2) 

    @property
    def number(self):
        return self._number
    
    @property
    def name(self):
        return self._name
    
    @property
    def lastname(self):
        return self._lastname

    @property
    def position(self):
        return self._position
    
    @property
    def height(self):
        return self._height
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def grade(self):
        return self._grade
    
    @property
    def town(self):
        return self._town
    
    @property
    def highschool(self):
        return self._highschool

    @property
    def score(self):
        return self._score
     
    def __repr__(self):
        return '{} - {} {}'.format(self.position, self.name, self.lastname)