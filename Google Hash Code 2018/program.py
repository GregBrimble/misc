from collections import Counter
from itertools import chain
import logging
import os
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

    def __init__(self, j, i, ingredient, top=False, right=False, bottom=False, left=False):
        self.j = j
        self.i = i
        self.ingredient = ingredient
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    # Applies a slice, creating the visual border on a cell for output
    def cut(self, slice):
        if slice.y1 == self.j and slice.x1 <= self.i <= slice.x2:
            self.top = True
        if slice.x2 == self.i and slice.y1 <= self.j <= slice.y2:
            self.right = True
        if slice.y2 == self.j and slice.x1 <= self.i <= slice.x2:
            self.bottom = True
        if slice.x1 == self.i and slice.y1 <= self.j <= slice.y2:
            self.left = True

    # Draws the cell for output - returns three lines (top, middle and bottom)
    def draw(self):

        lines = []

        for i in range(3):
            line = ""

            if self.left:
                line += "|"
            else:
                line += " "

            if i == 0 and self.top:
                line += "-"
            elif i == 1:
                line += self.ingredient
            elif i == 2 and self.bottom:
                line += "-"
            else:
                line += " "

            if self.right:
                line += "|"
            else:
                line += " "

            lines.append(line)

        return lines

    # Join an array of cell line outputs
    def join(outputs):
        lines = []
        for i in range(3):
            lines.append([output[i] for output in outputs])

        return lines


class Pizza:

    matrix = []
    bins = {}
    slices = []

    def __init__(self, file_name=None):
        if file_name:
            self.load(file_name)
            self.bin_count()

    def load(self, file_name):
        logging.info("Loading matrix from %s..." % file_name)

        with open(file_name, 'r') as f:
            r, c, self.l, self.h = list(map(int, f.readline().split(" ")))
            for j, line in enumerate(f):
                self.matrix.append([Cell(j, i, ingredient) for i, ingredient in enumerate(list(line)[:-1])])

        logging.info("Loading complete.")

    def output(self, display_matrix=False, display_slices=True, display_bins=True):
        logging.info("Outputing matrix to display...")

        print(" " * 24)
        print("-" * 24)
        print(" " * 24)

        if display_matrix:
            output_pizza = Pizza()
            output_pizza.matrix = self.matrix

            if not display_slices:
                output_pizza.slices = [] # [Slice(0, 0, len(output_pizza.matrix)-1, len(output_pizza.matrix[0])-1)]
            else:
                output_pizza.slices = self.slices

            for j, row in enumerate(output_pizza.matrix):
                outputs = []
                for i, cell in enumerate(row):
                    for slice in output_pizza.slices:
                        cell.cut(slice)
                    outputs.append(cell.draw())

                lines = Cell.join(outputs)

                for line in lines:
                    print("".join(line))

            print(" " * 24)
            print("-" * 24)
            print(" " * 24)

        if display_slices:
            for slice in self.slices:
                print("%i %i %i %i" % (slice.y1, slice.x1, slice.y2, slice.x2))

            print(" " * 24)
            print("-" * 24)
            print(" " * 24)

        if display_bins:
            for ingredient, count in self.bins.items():
                print("%s: %i" % (ingredient, count))

            print(" " * 24)
            print("-" * 24)
            print(" " * 24)

        logging.info("Output complete.")

    def bin_count(self):
        logging.info("Counting bins of matrix...")
        self.bins = Counter(cell.ingredient for cell in list(chain.from_iterable(self.matrix)))
        logging.info("Bin counting complete.")

    def slice(self, y1, x1, y2, x2):
        self.slices.append(Slice(y1, x1, y2, x2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Usage: python program.py [input file]")

    pizza = Pizza(sys.argv[1])
    pizza.slice(0, 0, 2, 1)
    pizza.slice(0, 2, 2, 2)
    pizza.slice(0, 3, 2, 4)
    pizza.output()
