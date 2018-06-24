#RAFAEL BROSEGHINI

#!/usr/bin/env python3
#encoding: UTF-8

import random
# Need a seed for randomization
# random.seed(42)

class Die:
    '''A die class'''
    def __init__(self, possible_values):
        self._possible_values = possible_values
        self._value = 1

    def roll(self):
        '''Roll the die'''
        self._value = random.choice(self._possible_values)
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _):
        if _ >= 1 and _ <= 6:
            self._value = _
        else:
            raise ValueError('Value is not acceptable for the use of a die.')        

    @value.deleter
    def value(self):
        ''''value' property deleter'''
        del self._value

    def __str__(self):
        '''__str__ override'''
        return str(self._value)

class Cup:
    def __init__(self, num_dice, num_sides_=6):
        self._dice = [Die(range(1, num_sides_ + 1)) for _ in range(num_dice)]

    def shake(self):
        for i in self._dice:
            print(i.roll())

    def remove(self, idx_):
        '''Remove a die from the cup'''
        self._dice.pop(idx_)

    def add(self, die_):
        '''Add a die to the cup'''
        self._dice.append(die_)

    def roll(self, *args):
        '''Roll the dice'''
        for i in args:
            if i > 0 and i <= len(args):
                self._dice[i-1].roll()

    def total(self):
        return sum([d._value for d in self._dice])

    def __len__(self):
        return len(self._dice)

    def __str__(self):
        '''__str__ override'''
        return str([i.value for i in self._dice])

    def __getitem__(self, idx):
        return self._dice[idx]

    def __iter__(self):
        '''Cup iterator'''
        return iter(self._dice)




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
