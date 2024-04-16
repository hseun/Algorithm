def solution(a, b):
    if a > b:
        a, b = b, a
    return sum([n for n in range(a, b + 1)])