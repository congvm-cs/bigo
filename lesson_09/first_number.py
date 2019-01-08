# Finding the first character of number

def getFirstChar(n):
    if n//10==0:    
        return n
    else:
        return getFirstChar(n//10)

x = int(input())
x = x if x >= 0 else -x
print(getFirstChar(x))