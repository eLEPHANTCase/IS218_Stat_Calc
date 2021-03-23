from mathOps import MathOps
# Calculator class

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = MathOps.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = MathOps.subtraction(a, b)
        return self.result

    def multiply(self, a,b ):
        self.result = MathOps.multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = MathOps.division(a, b)
        return self.result

    def squareroot(self, x):
        self.result = MathOps.squareRoot(x)
        return self.result

    def square(self, x):
        self.result = square(x*x)
        return self.result