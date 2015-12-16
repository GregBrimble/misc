# Imports

import numpy as np          # Numpy, a library to handle the matrix and mathematical operations
import itertools as it      # Itertools, a library to perform permutations and other iterations
from copy import deepcopy   # Deepcopy, a function that correctly creates a unique cloned instance of a list
import math                 # Math, a library containing advanced mathematical funcitons

# Generates list of blocks of 1s as per a rule

def blockGenerator(rule):
    
    list_of_blocks = []
    
    for number in rule:
        list_of_blocks.append([1] * number)     # Generate block, and add to row
        
    return list_of_blocks
    
# Intersperse a list with an item
    
def intersperse(list_of_items, interspersed_item):
    
    interspersed = []
    
    for item in list_of_items:
        interspersed.append(item)
        interspersed.append(interspersed_item)
        
    interspersed.pop()      # Pop off extra 'interspersed_item' at the end
    
    return interspersed
    
# Flattens a list of blocks into a single dimension list (e.g. [[1, 1, 1], [0], [1], [0], [0], [1, 1, 1, 1, 1]] => [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1])

def flatten(list_of_blocks):
    return list(it.chain.from_iterable(list_of_blocks))         # Lookup itertools for more info

# Compares a test_list against the known list, and returns if True if valid

def isValid(test_list, known_list):

    for i, element in enumerate(known_list):                # For each element in existing list,
        if element != -1 and test_list[i] != element:       # If it is known, and test_list doesn't match at it,
            return False                                    # Return false
            break                                           # Break for completeness
    
    return True                                             # Else return true
       
# Returns the indexes of constant values within a list

def constantValuesInList(list_to_check):

    constant_indexes = []
    
    for position in range(0, len(list_to_check[0])):
        if all(item_to_check[position] == list_to_check[0][position] for item_to_check in list_to_check):
            constant_indexes.append(position)
            
    return constant_indexes

# Returns a list a possibilities that match rule, and 

def generateValidPossibilities(known_list, list_rule, log10ofPermutations):

    list_of_blocks = blockGenerator(list_rule)
    
    list_of_interspersed_blocks = intersperse(list_of_blocks, [0])
    
    # Calculate number of [0]'s are still required to fully populate list
    
    num_to_add = len(known_list)
    
    for block in list_of_interspersed_blocks:
        num_to_add -= len(block)
        
    # For each possible index of the remaining [0]'s, create the row, check its validity against 'known_list', and add to list 'possibilities'
    
    possibilities = []
    
    if math.log10(math.factorial(len(list_of_interspersed_blocks) + num_to_add + 1) / math.factorial(len(list_of_interspersed_blocks) + 1)) < log10ofPermutations:
        for permutation_indexes in it.permutations(range(0, (len(list_of_interspersed_blocks) + num_to_add + 1)), num_to_add):     # Generate list of [0]'s potential indexes
            
            new_list = deepcopy(list_of_interspersed_blocks)        # Copy entire /list_of_interspersed_blocks'
            for permutation_index in permutation_indexes:
                new_list.insert(permutation_index, [0])             # Add [0]'s at each index
            new_list = flatten(new_list)    
            if isValid(new_list, known_list) == True:               # If new list is valid with existing 'known_list'
                possibilities.append(new_list)                      # Convert to 1D array and add to 'possibilities'
    
    return possibilities


""" INITIALISATION """

# Initialise the matrix as -1's to identify each element is unknown

matrix = np.empty([25, 25])
matrix.fill(-1)

""" KNOWN VALUES """

matrix[3, 3], matrix[3, 4], matrix[3, 12], matrix[3, 13], matrix[3, 21] = (1,)*5
matrix[8, 6], matrix[8, 7], matrix[8, 10], matrix[8, 14], matrix[8, 15], matrix[8, 18] = (1,)*6
matrix[16, 6], matrix[16, 11], matrix[16, 16], matrix[16, 20] = (1,)*4
matrix[21, 3], matrix[21, 4], matrix[21, 9], matrix[21, 10], matrix[21, 15], matrix[21, 20], matrix[21, 21] = (1,)*7

""" RULES """

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

                                                                                                # """ START HERE """

loop_number = 0                                                                                 # Loop for CPU time optimisation (see above)

while -1 in matrix:                                                                             # While the matrix isn't solved
    found = False                                                                               # Loop through, starting at 0, up to log10(25!) (see above)
    for i in range(0, matrix.shape[0]):                                                         # For each row and column, in matrix
    
                                                                                                # """ ROWS """
    
        if -1 in matrix[i,:]:                                                                   # If row isn't entirely solved
            row_possibilities = generateValidPossibilities(matrix[i,:], r[i], loop_number)      # Generate all valid possibilities that fit with rules and existing
            
            if len(row_possibilities) > 0:                                                      # If some possibilities found
                if len(row_possibilities) == 1:                                                 # But only one
                    matrix[i,:] = row_possibilities[0]                                          # Row is solved! Insert into matrix
                    print "r:", i, matrix[i,:]                                                  # Herald success
                    found = True                                                                # Flag success
                else:                                                                           # Otherwise, if more than one is found
                    constant_indexes = constantValuesInList(row_possibilities)                  # Look for any constant values in each possibility
                    for constant_index in constant_indexes:                                     # For each found
                        if matrix[i, constant_index] == -1:                                     # That wasn't already known
                            matrix[i, constant_index] = row_possibilities[0][constant_index]    # Value is solved! Insert into matrix
                            print "r:", i, "c:", constant_index, matrix[i, constant_index]      # Herald success
                            found = True                                                        # Flag success
                
                                                                                                # """ END ROWS """
                
        j = i                                                                                   # Move along diagonal from 0, 0 to n, n
        
                                                                                                # """ COLUMNS """
        
        if -1 in matrix[:,j]:                                                                   # If column isn't entirely solved
            column_possibilities = generateValidPossibilities(matrix[:,j], c[j], loop_number)   # Generate all valid possibilities that fit with rules and existing
            
            if len(column_possibilities) > 0:                                                   # If some possibilities found
                if len(column_possibilities) == 1:                                              # But only one
                    matrix[:,j] = column_possibilities[0]                                       # Column is solved! Insert into matrix
                    print "c:", j, matrix[:,j]                                                  # Herald success
                    found = True                                                                # Flag success
                else:                                                                           # Otherwise, if more than one is found
                    constant_indexes = constantValuesInList(column_possibilities)               # Look for any constant values in each possibility
                    for constant_index in constant_indexes:                                     # For each found
                        if matrix[constant_index, j] == -1:                                     # That wasn't already known
                            matrix[constant_index, j] = column_possibilities[0][constant_index] # Value is solved! Insert into matrix
                            print "r:", constant_index, "c:", j, matrix[constant_index, j]      # Herald success
                            found = True                                                        # Flag success
                            
                                                                                                # """ END COLUMNS """
                                                                                                
    if found != True:                                                                           # If interation bared no fruit
        loop_number += 1                                                                        # Try with more CPU time
    print loop_number                                                                           # Output desparation
    
print matrix
