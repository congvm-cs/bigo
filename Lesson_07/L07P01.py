# Appearance

def isExisted(x):
    d = set(['b', 'i', 'g', 'o'])
    if len(d.intersection(x)) != 0:
        return "YES"
    else:
        return "NO"

def checkAppearance(x):
    ret = []
    for _, i in enumerate(x):
        i = set(i.lower())
        ret.append(isExisted(i))
    return ret


n_lines = int(input())
input_list = []
for i in range(n_lines):
    input_list.append(str(input()))

for i in checkAppearance(input_list):
    print(i)