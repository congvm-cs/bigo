def normalize(x):
    x = x.split(' ')
    return " ".join([i for i in x[::-1]])


input = str(input()).strip()
print(normalize(input))
