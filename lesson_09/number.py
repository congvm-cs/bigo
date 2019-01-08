# Count characters in number
import sys
sys.setrecursionlimit(10000)

def count(n):
    if n//10 == 0:
        return 1
    else:
        return 1 + count(int(n//10))


x = int(input())
if x < 0:
    x = -x
    
print(count(x))