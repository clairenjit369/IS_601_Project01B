from Functions.addition import addition
from Functions.subtraction import subtraction
from Functions.multiplication import multiplication
from Functions.division import division
from Functions.square import square
from Functions.squareRoot import squareRoot


class Calculator:
    result = 0

    def __init__(self):
        pass

    @classmethod
    def add(self, a, b):
        self.result = addition.add(a, b)
        return self.result

    @classmethod
    def subtract(self, a, b):
        self.result = subtraction.sub(a, b)
        return self.result

    @classmethod
    def multiply(self, a, b):
        self.result = multiplication.mul(a, b)
        return self.result

    @classmethod
    def divide(self, a, b):
        self.result = division.div(a, b)
        return self.result

    @classmethod
    def square(self, a):
        self.result = square.square(a)
        return self.result

    #sq root method
    @classmethod
    def sqrt(self, a):
        self.result = squareRoot.squareRoot(a)
        return self.result
