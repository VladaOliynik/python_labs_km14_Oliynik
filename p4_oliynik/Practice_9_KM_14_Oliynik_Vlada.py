#import required modules

import numpy as np
from copy import copy

def check(arg: str) -> int:
    '''
    Func takes a string as a parameter and offers input
    Returns: integer number, if an integer is entered, otherwise it calls itself (recursion)
    '''

    message = input(f'Enter size(order) of {arg}: ')
    try:
        if int(message) == float(message):  #float check
            return int(message)
    except:
        print('Enter integer value!')
        return check(arg)

def random_matrix(dim: int):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

#calls check() func
size = check('matrix')

#convert np.array to list and create global var total
matrix = random_matrix(size).tolist()
total = 0

def det(A: list) -> int:
    '''
    Func takes a list value (matrix nxn), after copies the argument to a local variable,
    finds all permutations, after that counts the number of inversions for every element.

    After func recall itself (recursion)

    Last result returns to place func.
    '''
    global total, size

    # for 2x2 matrix
    if len(A) == 2 and len(A[0]) == 2:
        deter = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return deter

    for i in range(size):
        matrix_temp = copy(A)
        del matrix_temp[0]
        for j in range(len(matrix_temp)):
            #for every elements by cycle - find permutation (without itertools)
            matrix_temp[j] = matrix_temp[j][0:i] + matrix_temp[j][i + 1:]

        #for every elements by cucle - find sign (number of inversions)
        inversions_of_number = (-1) ** (i % 2)

        #recall func itself (recursion)
        elements_of_sum = det(matrix_temp)
        total += inversions_of_number * elements_of_sum * A[0][i]

    return total


print(f'Your matrix was:\n{matrix}')

#CALLS MY FUNC
print(f'Result: {det(matrix)}')

#CALL FOR CHECK
print(f'Checked my NumPy: {np.linalg.det(matrix)}')