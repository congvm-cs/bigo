# insertion sort

def insertion_sorted(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            if arr[j] > arr[j-1]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
            j -= 1
    return arr

# arr = [5, 1, 4, 6, 1, 0, 2, 10, 11, 15, 0, 2]
n = int(input())
arr = list(map(int, input().split()))

print(" ".join([str(i) for i in insertion_sorted(arr)]))