from die import Die


class Cup:
    def __init__(self, num_dice, num_sides_=6):
        self._dice = [Die(range(1, num_sides_ + 1)) for _ in range(num_dice)]

    def shake(self):
        for i in self._dice:
            print(i.roll())

    def add(self, die_):
        """Add a die to the cup"""
        self._dice.append(die_)

    def remove(self, idx_):
        """Remove a die from the cup"""
        self._dice.pop(idx_)

    def roll(self, *args):
        """Roll the dice"""
        for i in args:
            if 0 < i <= len(args):
                self._dice[i - 1].roll()

    def total(self):
        return sum([d._value for d in self._dice])

    def __len__(self):
        return len(self._dice)

    def __str__(self):
        """__str__ override"""
        return str([i.value for i in self._dice])

    def __getitem__(self, idx):
        return self._dice[idx]

    def __iter__(self):
        """Cup iterator"""
        return iter(self._dice)
