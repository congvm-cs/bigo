# is Number?

def isNumber(x):
    if str('0') <= str(x) and str(x) <= str('9'):
        return True
    else:
        return False

def numberCounter(x):
    counter = 0
    for _, i in enumerate(x):
        if isNumber(i):
            counter += 1
    return counter

input_str = str(input())
print(numberCounter(input_str))