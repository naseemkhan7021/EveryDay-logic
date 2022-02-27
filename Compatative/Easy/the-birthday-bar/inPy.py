# https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
# s = [2,2, 1, 3, 2]
s = [1, 2, 1, 3, 2]
d = 3
m = 2


def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if(sum(s[i:i+m]) == d):
            print(s[i:i+m])


birthday(s, d, m)
