# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
bill = [3, 10, 2, 9]
k = 1
b = 7


def bonAppetit(bill, k, b):
    bill.pop(k)
    if(sum(bill)//2) == b:
        return 'Bon Appetit'
    else:
        return abs((sum(bill)//2)-b)


print(bonAppetit(bill, k, b))
