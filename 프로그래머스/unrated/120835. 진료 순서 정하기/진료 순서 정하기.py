def solution(emergency):
    a = sorted(emergency)
    a.reverse()
    answer = []
    for i in emergency:
        answer.append(a.index(i) + 1)
    return answer