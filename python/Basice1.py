

# Matrix change in Zero
'''
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
'''

'''
# revers at position
arr0 = [10, 4, 5, 2, 3, 6, 1, 3, 6]
position = 3
ans = [10, 4, 5, 2, 3, 6, 1, 6, 3]
print(arr0[:3+1]+arr0[-1:3:-1])
'''

'''
#  find dublicat
sp_count = 0
dublicatArr = [3, 1, 3, 4, 2]
# dublicatArr_1 = [1, 3, 4, 2, 2]
# output ==> 2 , https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_1112602?leftPanelTab=1
for index_outer in range(0, len(dublicatArr)):
    for index_inner in range(index_outer+1, len(dublicatArr)):
        sp_count += 1
        print(sp_count)
        if(dublicatArr[index_outer] == dublicatArr[index_inner]):
            print(dublicatArr[index_outer])
        else:
            continue

print(sp_count)
'''


# Pair Sum
# https://www.codingninjas.com/codestudio/problems/pair-sum_697295
# arr = [1, 2, 3, 4, 5]
# arr = [2, -3, 3, 3, -2]
'''
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
'''

# Maximum Subarray Sum
# arr = [1, 2, 7, -4, 3, 2, -10, 9, 1]
# arr = [10, 20, -30, 40, -50, 60]
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# arr = [-2, -1]
# arr = [5, 4, -1, 7, 8]
# length = len(arr)
'''
all_Sum == a+arr[i]
b == arr[i]
max_Sum = a ? all_Sum>max_Sum : max_Sum
'''
#ans = a=a+b

'''
def maxSubarraySum(arr, n):
    max_Sum = 0
    all_Sum = 0
    i = 0
    while i < n:
        all_Sum += arr[i]
        if all_Sum < 0:
            all_Sum = 0
        if max_Sum < all_Sum:
            max_Sum = all_Sum
        i += 1
    return max_Sum
'''

'''
def maxSubarraySum(arr, n):
    max_Sum = 0
    all_Sum = 0
    i = 0
    while i < n:
        all_Sum += arr[i]
        if all_Sum < 0:
            all_Sum = 0
        if max_Sum < all_Sum:
            max_Sum = all_Sum
        i += 1
    return max_Sum


print(maxSubarraySum(arr, length))
'''

# print("{:.6f}". format(0/6), end='\n')
# print("{:.6f}". format(0/6),)


def isPalindrome(x: int) -> bool:
    s = 0
    tem = x
    while x > 0:
        r = x % 10
        s = (s*10)+r
        x //= 10
    print(tem, s, x)


isPalindrome(121)
