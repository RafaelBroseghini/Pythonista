import random

# Need a seed for randomization
# random.seed(42)


class Die(object):
    """A die class"""

    def __init__(self, possible_values):
        self._possible_values = possible_values
        self._value = 1

    def roll(self):
        """Roll the die"""
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
            raise ValueError("Value is not acceptable for the use of a die.")

    @value.deleter
    def value(self):
        """'value' property deleter"""
        del self._value

    def __str__(self):
        """__str__ override"""
        return str(self._value)
