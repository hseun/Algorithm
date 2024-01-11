def solution(n):
    answer = []
    a = 2
    while a <= n:
        if n == 1:
            return sorted(answer)
        elif n % a == 0:
            if a not in answer:
                answer.append(a)
            n = n // a
        else:
            a += 1
    return sorted(answer)