def solution(arr):
    count = 1
    while count < len(arr):
        count *= 2
    arr = arr + ([0] * (count - len(arr)))
    return arr