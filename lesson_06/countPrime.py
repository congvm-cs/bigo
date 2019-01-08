# count Prime
def isPrime(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def countPrimes(n):
    return sum([1 if (isPrime(i) == True) else 0 for i in n])

n_numbers = int(input())
l_numbers = list(map(int, input().split()))
print(countPrimes(l_numbers))