import sys

def recurse(n):
    print(n)
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
    if n == 2000:
        return
    recurse(n + 1)
