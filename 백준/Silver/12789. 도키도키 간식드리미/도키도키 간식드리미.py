import sys
input = sys.stdin.readline

stack = []
n = int(input())
line = list(map(int, input().split()))
counts = 1

for num in line:
    while stack and stack[-1] == counts:
        stack.pop()
        counts += 1
    if num == counts:
        counts += 1
    else:
        stack.append(num)
if stack == sorted(stack, reverse=True):
    print("Nice")
else:
    print("Sad")