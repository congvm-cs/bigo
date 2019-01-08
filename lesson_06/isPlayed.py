#isPlayed
def mySum(x):
    sum = 0
    for i in x:
        sum += i
    return sum

def isPlayed(n):
    total_male = mySum([1 if (i == 0) else 0 for i in n])
    total_female = mySum([1 if (i == 1) else 0 for i in n])
    return "YES" if total_male == total_female else "NO"

n_numbers = int(input())
l_numbers = list(map(int, input().split()))
print(isPlayed(l_numbers))