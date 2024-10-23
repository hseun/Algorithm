import sys
input = sys.stdin.readline

result = 0
n = int(input())
customers = sorted([int(input()) for _ in range(n)], reverse=True)
for i in range(n):
    tip = customers[i] - i
    if tip > 0:
        result += tip
print(result)