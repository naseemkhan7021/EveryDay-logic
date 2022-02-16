
# Maximum Subarray Sum
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# arr = [10, 20, -30, 40, -50, 60]
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr = [-2, -1]
# arr = [5, 4, -1, 7, 8]
# length = len(arr)
'''
all_Sum == a+arr[i]
b == arr[i]
max_Sum = a ? all_Sum>max_Sum : max_Sum
'''
#ans = a=a+b


def maxSubarraySum(arr, n):
    max_Sum, all_Sum, i = arr[0], arr[0], 0
    # print(max_Sum, all_Sum, i)
    while i < n:
        all_Sum = max(arr[i], all_Sum+arr[i])
        max_Sum = max(all_Sum, max_Sum)
        i += 1
    return max_Sum


print(maxSubarraySum(arr, len(arr)))
