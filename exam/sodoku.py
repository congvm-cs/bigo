def isValid(list_num):
    list_num = sorted(list_num)
    for i in range(len(list_num) - 1):
        if list_num[i] == list_num[i+1]:
            return False
    return True

def isValidSquare(arr, strike=3):
    for x in range(0, int(len(arr)/strike)):
        for y in range(0, int(len(arr)/strike)):
            window_arr = []
            for i in range(y*strike, y*strike + strike):
                for j in range(x*strike, x*strike + strike):
                    window_arr.append(arr[i][j])
            if not isValid(window_arr):
                return False
    return True

def isValidRow(arr):
    for y in arr:
        if not isValid(y):
            return False
    return True

def isValidColumn(arr):
    for x in range(0, len(arr)):
        row = []
        for y in range(0, len(arr)):    
            row.append(arr[x][y])
        
        if not isValid(row):
            return False
    return True

def isValidResult(arr):
    if not isValidColumn(arr):
        return "NO"
    
    elif not isValidRow(arr):
        return "NO"

    elif not isValidSquare(arr):
        return "NO"

    return "YES"

n = 9
arr = []
for i in range(n):
    row = []
    row.extend(list(map(int, input().split(' '))))
    arr.append(row)



# arr = [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

# arr = [
#     [4, 3, 6, 5, 2, 9, 7, 1, 8],
#     [1, 8, 9, 4, 6, 7, 2, 3, 5],
#     [7, 5, 2, 1, 8, 3, 6, 9, 4],
#     [3, 2, 7, 6, 9, 5, 4, 8, 1],
#     [5, 6, 4, 8, 7, 1, 9, 2, 3],
#     [9, 1, 8, 3, 4, 2, 5, 6, 7],
#     [2, 7, 3, 9, 1, 4, 8, 5, 6],
#     [1, 9, 1, 7, 5, 8, 3, 4, 2],
#     [8, 4, 5, 2, 3, 6, 1, 7, 9]
# ]

print(isValidResult(arr))