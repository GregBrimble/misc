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
        self.started_at = None
        self.done = False

    def __str__(self):
        return "{start} -> {finish}".format(start=self.start, finish=self.finish)

    def distance(self):
        return manhattanDist(self.start, self.finish)


class Car():

    def __init__(self, x, y):
        self.position = Coordinate(x, y)
        self.ride = None

    def __str__(self):
        return str(self.position)

    def assign_ride(self, timeStep, ride, distance):
        self.ride = ride
        self.ride.started_at = timeStep + distance

    def remaining_distance(self, timeStep):
        try:
            return self.ride.distance() + self.ride.started_at - timeStep
        except AttributeError:
            return 0


def manhattanDist(start, finish):
    return sum([abs(start.row-finish.row), abs(start.column-finish.column)])


def step(rides, cars, timeStep, submissions):

    distances = {}

    for ride in rides:
        if ride.done or ride.started_at:
            continue

        for car in cars:
            if car.ride:
                distances[car] = car.remaining_distance(timeStep) + manhattanDist(car.ride.finish, ride.start)
            else:
                distances[car] = manhattanDist(car.position, ride.start)

        nearest_car = min(distances, key=distances.get)

        if ride.latest_finish < (timeStep + ride.distance() + distances[nearest_car]):
            ride.done = True
            continue

        if ride.earliest_start > timeStep:
            continue

        if not nearest_car.ride:
            nearest_car.assign_ride(timeStep, ride, distances[nearest_car])
            continue

    for i, car in enumerate(cars):
        if car.remaining_distance(timeStep) == 0 and car.ride:
            car.position = car.ride.finish
            submissions[car].append(car.ride)
            car.ride = None


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    rides = []
    cars = []
    submission = {}
    with open("e_high_bonus.in") as f:
        R, C, F, N, B, T = list(map(int, f.readline().split(" ")))
        for j, line in enumerate(f):
            rides.append(Ride(*map(int, line.rstrip().split(" "))))

    for i in xrange(F):
        cars.append(Car(0, 0))

    for car in cars:
        submission[car] = []

    for timeStep in xrange(T):
        step(rides, cars, timeStep, submission)
        print("Time step", timeStep)

    print(submission)

    for car in cars:
        print("{length} {rides}".format(length=len(submission[car]), rides=" ".join((str(rides.index(ride)) for ride in submission[car]))))
