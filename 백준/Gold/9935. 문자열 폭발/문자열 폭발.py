import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
bomb_len = len(bomb)
stack = []
for c in s:
    stack.append(c)
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]
print(''.join(stack) if stack else "FRULA")