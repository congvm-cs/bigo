def countGroup(arr):
    counter = 1
    for i in range(1, (len(arr) - 1)):
        if arr[i] == arr[i+1]:
            counter += 1

    return counter

n = int(input())
arr = []
for i in range(n):
    arr.extend([i for i in input()])

print(countGroup(arr))