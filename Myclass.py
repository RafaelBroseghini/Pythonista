'''
Name: Rafael Broseghini
Prof: Roman Yasinovskyy

Purpose: Create a program that returns the winner of a soccer practice tournament based on the sum of all player's skill level on each team after reading every player's characteristics from players.txt

Course: CS-160
Date: 03/27/2017
'''
from collections import Counter
import random

# Implement Queue Data Structure that is going to be used later on.
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(random.randint(0, 10), item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
class Facility:
    def __init__(self, size):
        self._size = size
        
# Field is a Facility.       
class Field(Facility):
    def __init__(self, size, surface):
        super().__init__(size)
        self._surface = surface
    
    def __str__(self):
        return  self._size + "" + self._surface + ' fields.'
      
class Player():
    def __init__(self, name, lastname, grade, position, number, origin):
        self._name = name
        self._lastname = lastname
        self._grade = grade
        self._position = position
        self._number = number
        self._origin = origin
    
    @property
    def name(self):
        return self.name
    
    @property
    def lastname(self):
        return str(self.lastname)
    
    @property
    def grade(self):
        return self.grade
    
    @property
    def position(self):
        return self.position
    
    @property
    def number(self):
        return str(self._winscore)
    
    @property
    def origin(self):
        return self.origin
     
    def __repr__(self):
        return '{} {} number {} is a {} playing {} originally from {}'.format(self._name, self._lastname, self._grade, self._position, self._number, self._origin)
    # Reads from a file and evaluates each team skill based on the grade of each player within that team. Team with highest skill wins the tourney.
def main(): 
    myField = Field('30x50 yards ', 'grass')
    b = Queue()
    with open('players.txt', 'r') as players:
        print("Let's form 7 random teams for practice 5v5 games in " + str(myField))
        print()
        players.readline()
        for line in players:
            winner= []
            line_item = line.rstrip().split('\t')
            i = Player(line_item[1],line_item[2], line_item[0], line_item[6], line_item[3], line_item[8])
            b.enqueue(i)
        for myteam in range(7):
            all_players = []
            print('Team ' + str(myteam) + ' players: ')
            for myteam in range(5):
                team = []
                score = []
                fixing = b.dequeue()
                all_players.append(fixing)
            for i in all_players:   
                Sr_skill = 0
                Jr_skill = 0
                So_skill = 0
                Fr_skill = 0
                Team_skill = 0
                print(str(i))
                fixing = str(i).split(' ')
                if fixing[6] == 'a':
                    if fixing[7] == 'Sr':
                        team.append(fixing[7])
                        Sr_skill += 5
                    elif fixing[7] == 'Jr':
                        team.append(fixing[7])
                        Jr_skill += 4.5
                    elif fixing[7] == 'So':
                        team.append(fixing[7])
                        So_skill += 3.5
                    elif fixing[7] == 'Fr':
                        team.append(fixing[7])
                        Fr_skill += 2.75                  
                elif fixing[6] == 'Sr':
                    team.append(fixing[6])
                    Sr_skill += 5
                elif fixing[6] == 'Jr':
                    team.append(fixing[6])
                    Jr_skill += 4.5
                elif fixing[6] == 'So':
                    team.append(fixing[6])
                    So_skill += 3.5
                elif fixing[6] == 'Fr':
                    team.append(fixing[6])
                    Fr_skill += 2.75
                Team_skill = Sr_skill + Jr_skill + So_skill + Fr_skill
                score.append(Team_skill)
                Team_skill = str(sum(score))
            winner.append(Team_skill)
            mymax = winner.index(max(winner))
            print("This team skill level is: " + Team_skill)
            print()
        print('The winner of the 5v5 tournament is Team ' + str(mymax) +  ' with ' + max(winner) + ' points.')
                
main()

