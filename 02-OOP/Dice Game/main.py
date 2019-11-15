#!/usr/bin/env python3
# Author: Rafafel Broseghini

# encoding: UTF-8

from cup import Cup
from player import Player


def get_winner(scoreBoard, maxScore):
    for player in scoreBoard:
        if scoreBoard[player] == maxScore:
            return player


def game(p1, p2, num_dices_per_player, maxScore):
    scoreBoard = {p1.name: 0, p2.name: 0}
    i = 0
    while scoreBoard[p1.name] < maxScore and scoreBoard[p2.name] < maxScore:
        p1Roll = p1.cup[i].roll()
        p2Roll = p2.cup[i].roll()
        if p1Roll > p2Roll:
            scoreBoard[p1.name] += 1
        elif p1Roll == p2Roll:
            scoreBoard[p1.name] += 0
            scoreBoard[p2.name] += 0
        else:
            scoreBoard[p2.name] += 1
        i += 1
        if i == num_dices_per_player:
            i = 0

    winner = get_winner(scoreBoard, maxScore)
    return "....And the winner is: {} !!!".format(winner)


def main():
    """Entry point"""
    print("Let's play a game!\n")
    dices = int(input("How many die? "))
    points = int(input("How many points? "))

    p1 = Player("Rafa", Cup(dices))
    p2 = Player("Mo", Cup(dices))

    print(game(p1, p2, dices, points))


if __name__ == "__main__":
    main()
