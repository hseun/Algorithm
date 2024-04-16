def solution(n):
    answer = 0
    n = list(str(n))
    for num in n:
        answer += int(num)
    return answer