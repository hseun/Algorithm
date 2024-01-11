def solution(s):
    s = s.split()
    answer = 0
    num = int(s[0])
    for i in s:
        if i == 'Z':
            answer = answer - num
        else:
            answer += int(i)
            num = int(i)
    return answer