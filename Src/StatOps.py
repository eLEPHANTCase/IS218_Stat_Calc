import random

class RandomNumber:

    def __init__(self, start, finish):
        random.seed()
        self.start = start
        self.finish = finish
        self.result = None
        self.generateNumber()

    def generateNumber(self):

        if (type(self.start) is int or float) and (type(self.finish) is int or float)):
            self.result = random.uniform(self.start, self.finish)
        elif (type(self.start) is not int or float) and (type(self.finish) is not int or float)):
            self.result = "Must be two int values!"
        else: self.result = "Erroneous!"
        return self.result