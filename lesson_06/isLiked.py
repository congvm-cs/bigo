# isLiked
def isLiked(x):
    for i in x:
        if i == 0:
            return "NO"
    return "YES"

n = int(input())
l_numbers = list(map(int, input().split()))
print(isLiked(l_numbers))

