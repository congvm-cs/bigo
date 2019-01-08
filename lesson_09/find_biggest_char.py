def getBiggestChar(x, current_max):
    if x//10==0:
        return x if x>current_max else current_max
    else:
        return getBiggestChar(x//10, x%10 if x%10 > current_max else current_max)


x = int(input())
x = x if x>=0 else -x

max_val = x%10
print(getBiggestChar(x//10, max_val))