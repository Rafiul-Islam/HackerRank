import math


def average(array):
    # your code goes here
    array = list(set(array))
    return math.fsum(array) / len(array)
