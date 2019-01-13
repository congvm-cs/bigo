# Number Multiplication

def compute(a, b, c, d, n):
    p = a + b
    q = c + d
    ac = a*c
    bd = b*d
    pq = p*q
    adbc = pq - ac - bd
    return (10**n)*ac + (10**(n//2))*adbc + bd

def karatsuba(x, y):
    if len(str(x)) == 1 and len(str(y)) == 1:
        return x*y
    else:
        xmid = len(str(x))//2
        a = int(str(x)[:xmid])
        b = int(str(x)[xmid:])

        ymid = len(str(y))//2
        c = int(str(y)[:ymid])
        d = int(str(y)[ymid:])

        

x = 24
y = 10

