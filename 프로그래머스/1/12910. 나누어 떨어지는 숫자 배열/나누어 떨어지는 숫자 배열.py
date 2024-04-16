def solution(arr, divisor):
    arr = sorted([a for a in arr if a % divisor == 0])
    return arr if len(arr) != 0 else [-1]