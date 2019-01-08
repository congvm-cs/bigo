# String Normalization
# is Number?

# 11 12     3
# ffffff tt f
def isSpace(x):
    if x == ' ':
        return True
    else:
        return False

def normalize(x):
    ret = []

    status = False
    for _, i in enumerate(x):
        if isSpace(i) and status is False: # i is space and the prev. char is not space
            ret.append(i)
        elif not isSpace(i):
            ret.append(i)

        if isSpace(i):
            status = True
        else:
            status = False

    return "".join([i for i in ret])

input_str = str(input())
print(normalize(input_str.strip()))