def staircase(n):
    # Write your code here
    for i in range(1, n+1):
        print(" "*(n-i), end='')
        print("#"*i)


staircase(6)
