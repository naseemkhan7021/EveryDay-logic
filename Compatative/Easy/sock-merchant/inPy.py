# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
n = len(ar)


def sockMerchant(n, ar):
    newlist = list(set(ar))
    pairs = 0
    for i in newlist:
        pairs += ar.count(i)//2
    return pairs


print(sockMerchant(n, ar))
