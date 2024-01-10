def solution(my_string):
    answer = []
    for s in my_string:
        if '0' <= s and s <= '9':
            answer.append(int(s))
    answer.sort()
    return answer