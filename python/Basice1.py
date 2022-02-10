'''
# Matrix change in Zero
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# ==>==> [[1, 0, 1],[0, 0, 0],[1, 0, 1]]
matrix_copy1 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

row_index = 0
column_index = 0
find_row, find_column = 0, 0

col = 0



def changedItto_zero(col, row, column, arr):
    #     global col
    #     col += 1
    matrix_copy = arr[:]
    matrixLen = len(arr)
    for row_index in range(0, matrixLen):
        for column_index in range(0, len(matrix_copy[row_index])):
            matrix_copy[row][column_index] = 0
            matrix_copy[row_index][column] = 0
          #   break
     #    for item in matrix_copy:
     #        if item == -1:
     #            pass
    return (col, 'com -> ', matrix_copy)


def change(arr):
    global col
    matrixLen = len(arr)
    for row_index in range(0, matrixLen):
        for column_index in range(0, len(arr[row_index])):
            if(arr[row_index][column_index] == 0):
                find_row, find_column = row_index, column_index
                #   print('row ', find_row, ' col ', find_column)
                print('matx ', arr)
                col += 1
                return changedItto_zero(col, find_row, find_column, arr)
#    print(matrix[row_index])
print(change(matrix))
'''


'''
def changedItto_zero(col, row, column, arr):
    matrix_copy = matrix_copy1[:]
    matrixLen_row = len(matrix_copy1)
    matrixLen_col = len(matrix_copy1[0])
    for row_index in range(0, matrixLen_row):
        for column_index in range(0, matrixLen_col):
            matrix_copy[row][column_index] = 0
        matrix_copy[row_index][column] = 0
#     for row_index in range(0, matrixLen_row):
#         for column_index in range(0, matrixLen_col):
#             if matrix_copy[row_index][column_index] == -1:
#                 matrix_copy[row_index][column_index] = 0
    return matrix_copy


def change(arr):
    global col
    matrixLen_row = len(arr)
    matrixLen_col = len(arr[0])
    for row_index in range(0, matrixLen_row):
        for column_index in range(0, matrixLen_col):
            if(arr[row_index][column_index] == 0):
                find_row, find_column = row_index, column_index
                print('row ', find_row, ' col ', find_column)
               #  print('matx ', arr)
                col += 1
                finded = changedItto_zero(col, find_row, find_column, arr)
    return finded


print(change(matrix2))
'''


'''
# revers at position
arr0 = [10, 4, 5, 2, 3, 6, 1, 3, 6]
position = 3
ans = [10, 4, 5, 2, 3, 6, 1, 6, 3]
print(arr0[:3+1]+arr0[-1:3:-1])
'''

#  find dublicat
'''
dublicatArr = [3, 1, 3, 4, 2]
# dublicatArr_1 = [1, 3, 4, 2, 2]
# output ==> 2 , https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_1112602?leftPanelTab=1
for index_outer in range(0, len(dublicatArr)):
    for index_inner in range(index_outer+1, len(dublicatArr)):
        if(dublicatArr[index_outer] == dublicatArr[index_inner]):
            print(dublicatArr[index_outer])
        else:
            continue
'''

# Pair Sum
# https://www.codingninjas.com/codestudio/problems/pair-sum_697295
# arr = [1, 2, 3, 4, 5]
# arr = [2, -3, 3, 3, -2]
arr = [1, 4, 45, 6, 10, 8]
length = 6
find = 16


def pairSum(arr, s):
    arr2 = []
    for index1 in range(0, len(arr)):
        for index2 in range(index1+1, len(arr)):
            if arr[index1]+arr[index2] == s:
                arr2.append(arr[index1])
                arr2.append(arr[index2])
            else:
                continue
    return sorted(arr2)


print(pairSum(arr, find))
