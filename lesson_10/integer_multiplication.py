# The Grade-School Algorithm

# Input: x, y
# Output: x*y

def mul(x, y):
    return x*y


def mul_gradeschool(x, y):
    pad = 0 
    ret = 0
    n = len(str(y))
    while pad < n:
        r = y%10
        ret += r*x*(10**pad)
        pad+=1
        y = y//10
    return ret

x = 10213
y = 123

print(mul(x, y))
print(mul_gradeschool(x, y))