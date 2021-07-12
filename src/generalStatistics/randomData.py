from random import sample
from random import randint
from generalStatistics.randomPopulation import random_population


class RandomData:
    size = 0
    data = []
    pop = []

    def __init__(self):
        pass

    def r_size(self, a, b):
        self.size = randint(a, b)
        return self.size

    def r_data(self, a, b):
        self.data = sample(a, b)
        return self.data

    def r_pop(self, a, b, c):
        self.pop = random_population(a, b, c)
        return self.pop
