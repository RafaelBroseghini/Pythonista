from abc import ABC, abstractmethod


class Animal(ABC):
    """Default animal"""

    @abstractmethod
    def __init__(self, spec_, age_, color_):
        self._spec = spec_
        self._age = age_
        self._color = color_

    @abstractmethod
    def sound(self):
        """Make noise"""
        pass

    def __str__(self):
        """Convert to string"""
        return "{} {} ({} yo)".format(self._color, self._spec, self._age)


class Bird(Animal):
    """Bird class"""

    @abstractmethod
    def __init__(self, spec_, age_, color_, flying_):
        # Task 1a: call the constructor of the superclass
        super().__init__(spec_, age_, color_)
        # Task 1b: initialize private property _flying
        self._flying = flying_

    def __str__(self):
        # Task 1c: if a bird is flying, return "Flying" + super().__str__()
        if self._flying:
            return "Flying " + super().__str__()
        # Task 1d: if a bird if not a flying one, return "Non-flying " + super().__str__()
        else:
            return "Non-Flying " + super().__str__()


class Mammal(Animal):
    """Mammal class"""

    @abstractmethod
    def __init__(self, spec_, age_, color_, habitat_):
        # Task 2a: call the constructor of the superclass
        super().__init__(spec_, age_, color_)
        # Task 2b: initialize private property _habitat if habitat_ is "Land", "Sea", "Air", or "Tree"
        if habitat_ in ["Land", "Sea", "Air", "Tree"]:
            self._habitat = habitat_
        # Task 2c: raise a ValueError is the habitat_ value is invalid
        else:
            raise ValueError("invalid habitat")


class Parrot(Bird):
    """Parrot class"""

    def __init__(self, age_, color_, talking_):
        # Task 3a: call the constructor of the superclass with "Parrot" as species and flying set to True
        super().__init__("Parrot", age_, color_, True)
        # Task 3b: initialize private property _talking to talking_
        self._talking = talking_

    def sound(self):
        # Task 3c: if a parrot is talking, return "'Polly wants a cracker'"
        if self._talking:
            return "'Polly wants a cracker' "
        # Task 3d: if a parrot is talking, return "nothing" (word)
        return "nothing"


class Penguin(Bird):
    """Penguin class"""

    def __init__(self, age_, color_):
        super().__init__("Penguin", age_, color_, False)

    def sound(self):
        return "nothing"


class Canine(Mammal):
    """Canine class"""

    @abstractmethod
    def __init__(self, spec_, age_, color_, habitat_):
        super().__init__(spec_, age_, color_, habitat_)


class Feline(Mammal):
    """Feline class"""

    @abstractmethod
    def __init__(self, spec_, age_, color_, habitat_):
        super().__init__(spec_, age_, color_, habitat_)

    def sound(self):
        return "Meow!"


class Dog(Canine):
    """Dog class"""

    def __init__(self, age_, color_):
        # Task 4a: call the constructor of the superclass with "Dog" as species and habitat set to "Land"
        super().__init__("Dog", age_, color_, "Land")

    def sound(self):
        return "Woof!"
        # Task 4b: return "Woof!"


class HouseCat(Feline):
    """HouseCat class"""

    def __init__(self, age_, color_):
        super().__init__("House Cat", age_, color_, "Land")


class BobCat(Feline):
    """BobCat class"""

    def __init__(self, age_, color_, habitat_):
        # Task 5a: call the constructor of the superclass with "Bobcat" as species
        super().__init__("Bobcat", age_, color_, habitat_)

    def __str__(self):
        return (
            str(self._color)
            + " "
            + str(self._habitat)
            + " "
            + str(self._spec)
            + " "
            + "("
            + str(self._age)
            + " yo)"
        )
        # Task 5b: return string must include color, habitat, species, and age
