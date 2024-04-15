def solution(num, total):
    n = total // num
    answer = [n]
    if num % 2 == 0:
        a = num // 2
        answer.append(n + num // 2)
    else:
        a = num // 2 + 1
    for i in range(1, a):
        answer.extend([n - i, n + i])
    return sorted(answer)