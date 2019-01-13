def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    return merge(mergeSort(L), mergeSort(R))


def merge(L, R):
    big = -10000000000
    i = 0
    j = 0
    arr = []
    L.append(big)
    R.append(big)

    while i < len(L)-1 or j < len(R)-1:
        if L[i] > R[j]:
            arr.append(L[i])
            i += 1
        else:
            arr.append(R[j])
            j += 1
    return arr


# arr = [1, 2, 2, 1, 2, 4, 6, 7, 8, 3]
n = int(input())
arr = list(map(int, input().split()))
print(" ".join([str(i) for i in mergeSort(arr)]))
# print(mergeSort(arr))