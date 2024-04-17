def solution(price, money, count):
    answer = money - sum([price * n for n in range(1, count + 1)])
    return abs(answer) if answer < 0 else 0