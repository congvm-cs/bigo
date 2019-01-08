# String Normalization
def isSpace(x):
    if x == ' ':
        return True
    else:
        return False

def isDot(x):
    if x == '.':
        return True
    else:
        return False


def normalize(x):
    x = "  " + x
    ret = []
    for i in range(2, len(x)):
        if isDot(x[i-2]) and isSpace(x[i-1]):
            ret.append(x[i].upper())
        else:
            ret.append(x[i])
    return "".join([i for i in ret])


input = str(input()).strip()
print(normalize(input))
