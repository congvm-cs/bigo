def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

def find_first_prime(x, i):
    if i > len(x) - 1:
        return -1
    else:
        val = x[i]
        if isPrime(val):
            return i
        else:
            return find_first_prime(x, i+1) 
        


n = int(input())
x = list(map(int, input().split(' ')))

i = 0
print(find_first_prime(x, i))
