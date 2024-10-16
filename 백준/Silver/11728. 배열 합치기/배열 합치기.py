import sys
input = sys.stdin.readline

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = sorted(a + b)
[print(num, end=' ') for num in result]