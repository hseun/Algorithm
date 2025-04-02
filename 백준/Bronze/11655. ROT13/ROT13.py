import sys
input = sys.stdin.readline

def eng_to_code(alpha):
    n = ord(alpha) + 13
    if ord(alpha) <= 90 < n or ord(alpha) <= 122 < n:
        n -= 26
    return chr(n)

s = input().rstrip()
result = []
for alpha in s:
    if 65 <= ord(alpha) <= 90 or 97 <= ord(alpha) <= 122:
        result.append(eng_to_code(alpha))
    else:
        result.append(alpha)
print(''.join(result))