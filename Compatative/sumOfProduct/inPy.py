# if q == 1 then sume of int
# if q == 2 the product of int

def sumOrProduct(n, q):
    from functools import reduce
#     s = 0
    if(q == 1):
        return round((n*(n+1)/2))
    else:
        return reduce(lambda a, b: a*b, range(1, n+1))


print(sumOrProduct(4, 2))
