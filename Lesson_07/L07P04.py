# String Normalization
def isSpace(x):
    if x == ' ':
        return True
    else:
        return False

def normalize(x):
    ret = []
    status = True
    for _, i in enumerate(x):
        if not isSpace(i) and status is True: # i is not space and the prev. char is space
            ret.append(i.upper())
        else:
            ret.append(i.lower())
        if isSpace(i):
            status = True
        else:
            status = False

    return "".join([i for i in ret])


n_lines = int(input())
input_list = []

for i in range(n_lines):
    input_list.append(str(input()))

ret = [normalize(i) for i in input_list]
for i in ret:
    print(i)