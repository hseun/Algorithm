import sys
input = sys.stdin.readline

n, _, k = map(int, input().split())
result = 0
for _ in range(n):
    seat = input().strip().split('1')
    for s in seat:
        result += len(s) - k + 1 if len(s) >= k else 0
print(result)