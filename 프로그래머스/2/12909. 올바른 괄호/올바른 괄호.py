def solution(s):
    count = 0
    for a in s:
        if a == '(':
            count += 1
        elif count == 0:
            return False
        else:
            count -= 1
    if count != 0:
        return False
    return True