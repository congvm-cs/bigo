# sum

def isDividableBy2(x):
    ret = []
    for i in x:
        if i % 2 == 0:
            ret.append(i)
    return ret

n = int(input())
l_numbers = list(map(int, input().split()))
ret = isDividableBy2(l_numbers)

for i in ret:
    print("{}".format(i))