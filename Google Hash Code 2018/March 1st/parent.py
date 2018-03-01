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
        self.busy = False

    def __str__(self):
        return str(self.position)

    def assign_ride(self, timeStep, ride, distance):
        self.busy = True
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

        if ride.started_at or ride.done:
            break

        for car in cars:
            if car.busy:
                break
            # if car.ride:
            #     distances[car] = car.remaining_distance(timeStep) + manhattanDist(car.ride.finish, ride.start)
            else:
                print(car, car.busy)
                distances[car] = manhattanDist(car.position, ride.start)

        try:
            print(distances)
            nearest_car = min(distances, key=distances.get)

            if ride.latest_finish < (timeStep + ride.distance() + distances[nearest_car]):
                ride.done = True
                break

            print("Assigning", nearest_car, ride, distances[nearest_car], timeStep)
            nearest_car.assign_ride(timeStep, ride, distances[nearest_car])
            for car in cars:
                print(car, car.busy)
        except ValueError:
            break

    for i, car in enumerate(cars):
        # print(i, car.ride, car.ride.started_at)
        if car.remaining_distance(timeStep) == 0 and car.ride:
            print("Clearing car", car)
            car.position = car.ride.finish
            submissions[car].append(car.ride)
            car.busy = False
            car.ride = None



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

    for car in cars:
        submission[car] = []

    for i in xrange(T):
        step(rides, cars, i, submission)
        print("Time step:", i)

    print(submission)
    for i, k in submission.items():
        print(i)
        for ride in k:
            print(ride)
