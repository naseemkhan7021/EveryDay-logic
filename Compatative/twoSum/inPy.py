# Pair Sum
# https://www.codingninjas.com/codestudio/problems/two-sum_839653
# arr = [1, 2, 3, 4, 5]
# arr = [2, -3, 3, 3, -2]
# arr = [0, -1, 2, -3, 1]
arr = [1, 4, 45, 6, 10, 8]
# arr = [1, 4, 6, 8, 10, 45]
# arr = [1, -1, -1, 2, 2]
# arr = [1, -2, 1, 0, 5]
find = 16

# O(n)


def twoSum(arr, target):
    # Write your code here.
    arr = sorted(arr)
    print(arr)
    arr2 = []
    start, end = 0, len(arr)-1

    while start < end:
        if(arr[start]+arr[end] == target):
            arr2.append((arr[start], arr[end]))
            start += 1
            end -= 1
        elif(arr[start]+arr[end] < target):
            start += 1
        else:
            end -= 1
    if len(arr2) == 0:
        return [(-1, -1)]
    return arr2


def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))


printAns(twoSum(arr, find))
# print(twoSum(arr, find))
