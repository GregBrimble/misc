from collections import Counter
from itertools import chain
import logging
import sys

class Slice:

    y1, x1, y2, x2 = (None, None, None, None)

    def __init__(self, y1=None, x1=None, y2=None, x2=None):
        self.set_all(y1, x1, y2, x2)

    def set_y1(self, y1):
        if self.y2:
            try:
                assert(y1 <= self.y2)
            except AssertionError:
                logging.warning("y1 is being set to a value greater than y2.")

        self.y1 = y1

    def set_x1(self, x1):
        if self.x2:
            try:
                assert(x1 <= self.x2)
            except AssertionError:
                logging.warning("x1 is being set to a value greater than x2.")

        self.x1 = x1

    def set_y2(self, y2):
        if self.y1:
            try:
                assert(y2 >= self.y1)
            except AssertionError:
                logging.warning("y2 is being set to a value less than y1.")

        self.y2 = y2

    def set_x2(self, x2):
        if self.x1:
            try:
                assert(x2 >= self.x1)
            except AssertionError:
                logging.warning("x2 is being set to a value less than x1.")

        self.x2 = x2

    def set_all(self, y1, x1, y2, x2):
        self.set_y1(y1)
        self.set_x1(x1)
        self.set_y2(y2)
        self.set_x2(x2)


class Cell:

    def __init__(self, ingredient):
        self.ingredient = ingredient


class Pizza:

    matrix = []
    slices = []
    bins = {}
    hills = []
    valleys = []

    def __init__(self, file_name=None):
        if file_name:
            self.load(file_name)
            self.bin_count()

    def load(self, file_name):
        logging.info("Loading matrix from %s..." % file_name)

        with open(file_name, 'r') as f:
            r, c, self.l, self.h = list(map(int, f.readline().split(" ")))
            for j, line in enumerate(f):
                self.matrix.append([Cell(ingredient) for ingredient in list(line)[:-1]])

        logging.info("Loaded.")

    def output(self, display_slices=True, display_bins=True, display_hills=True, display_valleys=False):
        logging.info("Generating output...")

        print(" " * 24)
        print("-" * 24)
        print(" " * 24)

        if display_bins:
            print("Bins")
            for ingredient, count in self.bins.items():
                print("%s: %i" % (ingredient, count))

            print(" " * 24)
            print("-" * 24)
            print(" " * 24)

        if display_hills:
            print("Hills")
            for hill in self.hills:
                print("[%i, %i]" % (hill[0], hill[1]))

            print(" " * 24)
            print("-" * 24)
            print(" " * 24)

        if display_valleys:
            print("Valleys")
            for valley in self.valleys:
                print("[%i, %i]" % (valley[0], valley[1]))

            print(" " * 24)
            print("-" * 24)
            print(" " * 24)

        if display_slices:
            print("Slices")
            for slice in self.slices:
                print("%i %i %i %i" % (slice.y1, slice.x1, slice.y2, slice.x2))

            print(" " * 24)
            print("-" * 24)
            print(" " * 24)

        logging.info("Output generated.")

    def bin_count(self):
        logging.info("Calculating bins...")
        self.bins = Counter(cell.ingredient for cell in list(chain.from_iterable(self.matrix)))
        logging.info("Bins calculated.")

    def map(self):
        logging.info("Calculating topography...")

        if not self.bins:
            self.bin_count()

        hill_ingredient = min(self.bins)
        valley_ingredient = max(self.bins)

        for j, row in enumerate(self.matrix):
            for i, cell in enumerate(row):
                if cell.ingredient == hill_ingredient:
                    self.hills.append([j, i])
                elif cell.ingredient == valley_ingredient:
                    self.valleys.append([j, i])

        logging.info("Topography calculated.")


    def slice(self, y1, x1, y2, x2):
        self.slices.append(Slice(y1, x1, y2, x2))


if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        logging.error("Usage: python program.py [input file] [verbosity=WARNING]")

    if sys.argv[2] == "DEBUG":
        level = logging.DEBUG
    elif sys.argv[2] == "INFO":
        level = logging.INFO
    elif sys.argv[2] == "WARNING":
        level = logging.WARNING
    elif sys.argv[2] == "ERROR":
        level = logging.ERROR
    elif sys.argv[2] == "CRITICAL":
        level = logging.CRITICAL

    logging.basicConfig(level=level)

    pizza = Pizza(sys.argv[1])
    pizza.map()
    pizza.output()
