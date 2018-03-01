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
        self.done = False

    def distance(self):
        return manhattanDist(self.start, self.finish)


class Car():

    def __init__(self, x, y):
        self.position = Coordinate(x, y)
        self.ride = None

    def __str__(self):
        return str(self.position)

    def remaining_distance(self):
        try:
            return manhattanDist(self.position, self.ride.finish)
        except AttributeError:
            return 0


def manhattanDist(start, finish):
    return sum([start.row, start.column, finish.row, finish.column])


def step(rides, cars, timeStep, submission):

    for ride in rides:
        if ride.done:
            break

        distances = {}

        for car in cars:
            if car.ride:
                distances[car] = car.remaining_distance() + manhattanDist(car.ride.finish, ride.start)
            else:
                distances[car] = manhattanDist(car.position, ride.start)

        nearest_car = min(distances, key=distances.get)

        if ride.latest_finish > (timeStep + ride.distance() + manhattanDist(nearest_car.position, ride.start)):
            ride.done = True
            break


    for car in cars:



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    rides = []
    cars = []
    submission = {}
    with open("a_example.in") as f:
        R, C, F, N, B, T = list(map(int, f.readline().split(" ")))
        for j, line in enumerate(f):
            rides.append(Ride(*map(int, line.rstrip().split(" "))))

    for i in xrange(F):
        cars.append(Car(0, 0))

    for i in xrange(T):
        step(rides, cars, i, submission)
