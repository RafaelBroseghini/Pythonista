#!/usr/bin/env python3
#Author: Rafafel Broseghini

#encoding: UTF-8

from cup import Cup

def game(num_dices_per_player, maxScore):
    p1 = Cup(num_dices_per_player)
    p2 = Cup(num_dices_per_player)
    scoreBoard = {p1: 0, p2: 0}
    i = 0
    while scoreBoard[p1] < maxScore and scoreBoard[p2] < maxScore:
        p1Roll = p1[i].roll()
        p2Roll = p2[i].roll()
        if p1Roll > p2Roll:
            scoreBoard[p1] += 1
        elif p1Roll == p2Roll:
            scoreBoard[p1] += 0
            scoreBoard[p2] += 0
        else:
            scoreBoard[p2] += 1
        i += 1
        if i == num_dices_per_player:
            i = 0
    return "The winner is: {}".format(scoreBoard)

def main():
    '''Entry point'''
    print("Let's play a game!")
    print(game(10,100))

if __name__ == "__main__":
    main()
