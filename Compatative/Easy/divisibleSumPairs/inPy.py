# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# ar = [1, 3, 2, 6, 1, 2]
ar = [1, 2, 3, 4, 5, 6]
k = 5
n = len(ar)


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
         
        for j in range(i+1, n):
            if ((ar[i]+ar[j]) % k == 0):
                count += 1
    return count


print(divisibleSumPairs(n, k, ar))
