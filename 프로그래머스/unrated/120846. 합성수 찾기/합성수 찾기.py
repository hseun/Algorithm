def solution(n):
    li = [a for a in range(2, n + 1)]
    prime = []
    if n == 1 or n == 2:
        return 0
    while li[0] ** 2 <= n:
        prime.append(li[0])
        li = [a for a in li if a % li[0] != 0]
    prime.extend(li)
    answer = n - (len(prime) + 1)
    return answer