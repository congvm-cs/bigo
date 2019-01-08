def unique(x):
    upper_ret = []
    lower_ret = []
    for _, i in enumerate(x):
        if i not in upper_ret and i.isupper(): 
            upper_ret.append(i)
        elif i not in lower_ret and i.islower():
            lower_ret.append(i)
    return sorted(upper_ret), sorted(lower_ret)

#==============================================#
input_str = str(input()).strip()
upper_ret, lower_ret = unique(input_str)
print(len(upper_ret) + len(lower_ret))