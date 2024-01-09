def solution(rsp):
    answer = ''
    rsp = list(rsp)
    for a in rsp:
        if a == '0':
            answer += '5'
        elif a == '2':
            answer += '0'
        elif a == '5':
            answer += '2'
    return answer