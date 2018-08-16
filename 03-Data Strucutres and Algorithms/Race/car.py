import random

class Car(object):
    def __init__(self, model):
        self.model = model
        self.distance = 0
    
    def accelerate(self):
        value=random.randint(1,5)
        self.distance += value
    
    def __str__(self):
        return "{} has covered {}m.".format(self.model, self.distance)
