# Pair Sum
# https://www.codingninjas.com/codestudio/problems/pair-sum_697295
# arr = [1, 2, 3, 4, 5]
# arr = [2, -3, 3, 3, -2]
# arr = [0, -1, 2, -3, 1]
# arr = [1, 4, 45, 6, 10, 8]
arr = [1, 4, 45, 6, 10, -8]
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
