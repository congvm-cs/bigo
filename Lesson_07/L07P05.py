def unique(x):
    upper_ret = []
    lower_ret = []
    for _, i in enumerate(x):
        if i not in upper_ret and i.isupper(): 
            upper_ret.append(i)
        elif i not in lower_ret and i.islower():
            lower_ret.append(i)
    return sorted(upper_ret), sorted(lower_ret)

def argMin(x):
    min_val = x[0]
    min_idx = 0
    for idx, val in enumerate(x):
        if val < min_val:
            min_val = val
            min_idx = idx
    return min_idx


def charCount(x):
    upper_ret, lower_ret = unique(x)    
    lower_counter = [0]*len(lower_ret)
    upper_counter = [0]*len(upper_ret)

    for i in x:
        for idx, j in enumerate(upper_ret):
            if i == j:
                upper_counter[idx]+=1
        
        for idx, j in enumerate(lower_ret):
            if i == j:
                lower_counter[idx]+=1
    
    if len(upper_ret) == 0:
        return str(lower_ret[argMin(lower_counter)]).upper()
    else:
        return str(upper_ret[argMin(upper_counter)]).upper()

#==============================================#
n_lines = int(input())
input_list = []

for i in range(n_lines):
    input_list.append(str(input()))

ret = [charCount(i.lower()) for i in input_list]
for i in ret:
    print(i)