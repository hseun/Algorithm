def solution(s):
    engNum = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for a in engNum:
        s = s.replace(a, str(engNum.index(a)))
    return int(s)