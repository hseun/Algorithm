def solution(array, height):
    high = [a for a in array if a > height]
    return len(high)