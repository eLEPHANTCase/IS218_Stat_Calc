# Operations for Calculator

class Arithmetic:

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
    def multiply(a, b):
        result = (a * b)
        return result