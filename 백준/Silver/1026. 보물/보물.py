import sys

input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()), reverse=True)
b = sorted(map(int, input().split()))
result = sum(x * y for x, y in zip(a, b))
print(result)