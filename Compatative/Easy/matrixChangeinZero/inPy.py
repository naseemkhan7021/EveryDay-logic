# Matrix change in Zero
from copy import deepcopy
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# ==>==> [[1, 0, 1],[0, 0, 0],[1, 0, 1]]
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# ==>==> [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

col = 0
matrixLen_row = len(matrix2)
matrixLen_col = len(matrix2[0])
matrix_copy = deepcopy(matrix2)

def changedItto_zero(row, column):
    # matrixLen_row = len(matrix2)
    # matrixLen_col = len(matrix2[0])
    for row_index in range(0, matrixLen_row):
        for column_index in range(0, matrixLen_col):
            matrix_copy[row][column_index] = 0
        matrix_copy[row_index][column] = 0
    return matrix_copy


def change(arr):
    global col
    # matrixLen_row = len(arr)
    # matrixLen_col = len(arr[0])
    for row_index in range(0, matrixLen_row):
        for column_index in range(0, matrixLen_col):
            if(arr[row_index][column_index] == 0):
                find_row, find_column = row_index, column_index
                print('row ', find_row, ' col ', find_column)
                print('matx ', arr)
                col += 1
                finded = changedItto_zero(find_row, find_column)
    return finded


print(change(matrix2))