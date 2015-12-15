# Imports

import numpy as np          # Numpy, a library to handle the matrix and mathematical operations
import itertools as it      # Itertools, a library to perform permutations and other iterations

# Generates list of blocks of 1s as per a rule

def ruleGenerator(rule):
    
    list_of_blocks = []
    
    for number in rule:
        list_of_blocks.append([1] * number)
        
    return list_of_blocks

def populateBlocks(list_of_blocks):
    
    num_of_zeros = 25
    
    for block in list_of_blocks:
        num_of_zeros -= len(block)
    
    print num_of_zeros


def possibilities(list):

    possibilities_list = []

    known_indexes = []
    
    for i, element in enumerate(list):
        if element != -1:
            known_indexes.append(i)
            
    
    
    #for possibility in it.product([
    
    """
    for possibility in it.product([0, 1], repeat=25-len(known_indexes)):
        for known_index in known_indexes:
            possibility.insert(known_index, list[known_index])
            ruleChecker(possibility, rule)
                #possibilities_list.append(possibility)
        
        print possibility
    
    exit()
    """
    #return possibilities_list

# Initialise the matrix as -1's to identify each element is unknown

matrix = np.empty([25, 25])
matrix.fill(-1)

# Fill in known 1's (blacks) in matrix

matrix[3, 3], matrix[3, 4], matrix[3, 12], matrix[3, 13], matrix[3, 21] = (1,)*5
matrix[8, 6], matrix[8, 7], matrix[8, 10], matrix[8, 14], matrix[8, 15], matrix[8, 18] = (1,)*6
matrix[16, 6], matrix[16, 11], matrix[16, 16], matrix[16, 20] = (1,)*4
matrix[21, 3], matrix[21, 4], matrix[21, 9], matrix[21, 10], matrix[21, 15], matrix[21, 20], matrix[21, 21] = (1,)*7

# Initialise known rules of elements of matrix
# Row rules

r = []

r.append([7, 3, 1, 1, 7])
r.append([1, 1, 2, 2, 1, 1])
r.append([1, 3, 1, 3, 1, 1, 3, 1])
r.append([1, 3, 1, 1, 6, 1, 3, 1])
r.append([1, 3, 1, 5, 2, 1, 3, 1])
r.append([1, 1, 2, 1, 1])
r.append([7, 1, 1, 1, 1, 1, 7])
r.append([3, 3])
r.append([1, 2, 3, 1, 1, 3, 1, 1, 2])
r.append([1, 1, 3, 2, 1, 1])
r.append([4, 1, 4, 2, 1, 2])
r.append([1, 1, 1, 1, 1, 4, 1, 3])
r.append([2, 1, 1, 1, 2, 5])
r.append([3, 2, 2, 6, 3, 1])
r.append([1, 9, 1, 1, 2, 1])
r.append([2, 1, 2, 2, 3, 1])
r.append([3, 1, 1, 1, 1, 5, 1])
r.append([1, 2, 2, 5])
r.append([7, 1, 2, 1, 1, 1, 3])
r.append([1, 1, 2, 1, 2, 2, 1])
r.append([1, 3, 1, 4, 5, 1])
r.append([1, 3, 1, 3, 10, 2])
r.append([1, 3, 1, 1, 6, 6])
r.append([1, 1, 2, 1, 1, 2])
r.append([7, 2, 1, 2, 5])

# Column rules

c = []

c.append([7, 2, 1, 1, 7])
c.append([1, 1, 2, 2, 1, 1])
c.append([1, 3, 1, 3, 1, 3, 1, 3, 1])
c.append([1, 3, 1, 1, 5, 1, 3, 1])
c.append([1, 3, 1, 1, 4, 1, 3, 1])
c.append([1, 1, 1, 2, 1, 1])
c.append([7, 1, 1, 1, 1, 1, 7])
c.append([1, 1, 3])
c.append([2, 1, 2, 1, 8, 2, 1])
c.append([2, 2, 1, 2, 1, 1, 1, 2])
c.append([1, 7, 3, 2, 1])
c.append([1, 2, 3, 1, 1, 1, 1, 1])
c.append([4, 1, 1, 2, 6])
c.append([3, 3, 1, 1, 1, 3, 1])
c.append([1, 2, 5, 2, 2])
c.append([2, 2, 1, 1, 1, 1, 1, 2, 1])
c.append([1, 3, 3, 2, 1, 8, 1])
c.append([6, 2, 1])
c.append([7, 1, 4, 1, 1, 3])
c.append([1, 1, 1, 1, 4])
c.append([1, 3, 1, 3, 7, 4])
c.append([1, 3, 1, 1, 1, 2, 1, 1, 4])
c.append([1, 3, 1, 4, 3, 3])
c.append([1, 1, 2, 2, 2, 6, 1])
c.append([7, 1, 3, 2, 1, 1])

populateBlocks(ruleGenerator(r[0]))

"""
# Enumerate through matrix until all are known
#while -1 in matrix:                                     # While there are unknowns
for (i, j), element in np.ndenumerate(matrix):      # Enumerate through entire matrix by every element, row then column
    if element == -1:                               # If element is unknown
            
            # Get row and column and relevant rules
            
            row = matrix[i,:]
            column = matrix[:,j]
            
            row_rules = r[i]
            column_rules = c[j]
            
            possibilities(row)
            possibilities(column)
"""
