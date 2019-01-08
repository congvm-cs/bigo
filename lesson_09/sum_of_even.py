def reduce_sum(x):
    if len(x) == 0:
        return 0
    else:
        val = x[0]
        x.remove(val)
        if val % 2 != 0:
            return reduce_sum(x)
        else:
            return val + reduce_sum(x)

n = int(input())
x = list(map(int, input().split(" ")))
print(reduce_sum(x))