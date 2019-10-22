from player import Player
class Roster():
    def __init__(self, roster=[]):
        self._roster = roster
        with open("players.txt") as file:
            for line in file:
                line = line.split(",")
                p = Player(line[0], line[1],line[2],line[3],line[4],
                           line[5],line[6],line[7],line[8])
                self._roster.append(p)

    @property
    def roster(self):
        return self._roster