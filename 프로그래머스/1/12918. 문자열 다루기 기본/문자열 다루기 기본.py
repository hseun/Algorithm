def solution(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if (len(s) == 4 or len(s) == 6) and s.isdecimal():
        return True
    return False