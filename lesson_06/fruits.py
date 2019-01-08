# min

def myMax(x):
    """ Find the maximal value in array
        Parameters:
            x: array
        Return: [idx, val]
    """
    max = x[0]
    pos = 0
    for idx, num in enumerate(x):
        if max < num:
            max = num 
            pos = idx
    return pos, max


def chooseBagOfFruits(x):
    choice = 1
    max_idx, maxApple = myMax([x[i] for i in range(0, len(x), 2)])
    
    print("MA ", maxApple)
    max_idx = max_idx*2
    maxOrange = x[max_idx + 1]

    print("MO ", maxOrange)
    for i in range(0, len(x), 2):
        if x[i] == maxApple and x[i+1] > maxOrange:
            choice = i//2 + 1
            maxOrange = x[i+1]
    return int(choice)


n = int(input())
l_numbers = []
for i in range(n):
    l_numbers.extend(list(map(int, input().split())))

print(l_numbers)

print(chooseBagOfFruits(l_numbers))

# print(myMax(l_numbers))