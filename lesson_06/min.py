# min
def findMinIndex(x):
    # Special case
    if len(x) == 1 and x[0] == 1:
        return x[-1] + 1

    elif len(x) == 1 and x[0] != 1:
        return 1
        
    else:
        for i in range(len(x) - 1):
            if x[i] + 1 != x[i+1]:
                return x[i] + 1
        return x[-1] + 1


n = int(input())
l_numbers = list(sorted(map(int, input().split())))
print(findMinIndex(l_numbers))