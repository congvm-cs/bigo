#trim Flower

def myMin(x):
    min = x[0]
    for i in x:
        if min > i:
            min = i
    return min

def mySum(x):
    sum = 0
    for i in x:
        sum += i
    return sum

def trimFlower(n):
    mini = myMin(n)
    total_effort = mySum([i - mini for i in n])
    return total_effort

n_numbers = int(input())
l_numbers = list(map(int, input().split()))
print(trimFlower(l_numbers))