# sum

def mySum(x):
    sum = 0
    for i in x:
        sum += i
    return sum

n = int(input())
l_numbers = map(int, input().split())
print(mySum(l_numbers))