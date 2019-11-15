#!/usr/bin/env python

"""
Name: Rafael Broseghini
Implementation of a 'Soccer Tournament' using data
from the LCMS website stored in a text file.
"""

import random
from team import Team
from tournament import Tournament
from roster import Roster
from player import Player


class Facility:
    def __init__(self, size):
        self._size = size


# Field is a Facility.
class Field(Facility):
    def __init__(self, size, surface):
        super().__init__(size)
        self._surface = surface

    def __str__(self):
        return self._size + "" + self._surface + " fields."


def main():
    f = Field("30x50 yards ", "grass")
    all_players = Roster()
    r = all_players.roster
    tourney = Tournament()
    divided_teams = tourney.make_teams(r)
    # # print(test)
    winner = tourney.compute_winner()

    print("These are the teams:\n")
    for t in range(len(divided_teams)):
        print("{}\n".format(divided_teams[t]))

    print("The winner is: \033[1;32m{}\033[0m".format(winner))


if __name__ == "__main__":
    main()
