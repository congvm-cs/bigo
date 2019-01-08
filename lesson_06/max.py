# sum

def myMax(x):
    max = x[0]
    for i in x:
        if max < i:
            max = i
    return max

n = int(input())
l_numbers = list(map(int, input().split()))
print(myMax(l_numbers))