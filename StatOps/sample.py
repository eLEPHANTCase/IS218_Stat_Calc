import random


def makeSample(sequence, size):
    '''Make a random sample by making use of sample() from the default library, random.'''
    sampleValues = random.sample(sequence, size)
    return sampleValues