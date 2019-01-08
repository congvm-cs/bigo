def find_odd_divisor(x):
    if x % 2 != 0:
        return x
    else:
        return find_odd_divisor(int(x/2))

x = int(input())
print(find_odd_divisor(x))


