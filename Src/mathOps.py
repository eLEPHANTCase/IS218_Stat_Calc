import math
import numpy

# Operations for Calculator

class MathOps:

    @staticmethod
    def addition(a, b):
        result = (a + b)
        return result

    @staticmethod
    def subtraction(a, b):
        result = (a - b)
        return result

    @staticmethod
    def division(a, b):
        try:
            result = float(a) / float(b)
            return result
        except ZeroDivisionError:
            raise ZeroDivisionError

    @staticmethod
    def multiplication(a, b):
        result = (a * b)
        return result

    @staticmethod
    def squareRoot(a):
        result = math.sqrt(a)
        return result

    @staticmethod
    def square(a):
        result = (a*a)
        return result
