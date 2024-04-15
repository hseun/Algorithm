def solution(arr):
    if arr.count(2) == 0:
        return [-1]
    elif arr.count(2) == 1:
        return [2]
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == 2:
            return arr[arr.index(2):i + 1]