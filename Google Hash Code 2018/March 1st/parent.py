from collections import Counter
from itertools import chain
import logging


class Coordinate():

    def __init__(self, x, y):
        self.row = x
        self.column = y

    def __str__(self):
        return "[Row, Column]: [{x}, {y}]".format(x=self.row, y=self.column)


class Ride():

    def __init__(self, a, b, x, y, s, f):
        self.start = Coordinate(a, b)
        self.finish = Coordinate(x, y)
        self.earliest_start = s
        self.latest_finish = f

    def distance(self):
        pass


class Car():

    def __init__(self, x, y):
        self.position = Coordinate(x, y)

    def __str__(self):
        return str(self.position)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    rides = []
    cars = []
    with open("a_example.in") as f:
        R, C, F, N, B, T = list(map(int, f.readline().split(" ")))
        for j, line in enumerate(f):
            rides.append(Ride(*line.rstrip().split(" ")))

    for i in xrange(F):
        cars.append(Car(0, 0))
