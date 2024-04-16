def solution(a, b):
    if a < b:
        return sum([n for n in range(a, b + 1)])
    return sum([n for n in range(b, a + 1)])