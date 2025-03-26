import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes = sorted(ropes, reverse=True)
max_weight = ropes[0]
for i in range(1, n):
    if ropes[i] * (i + 1) > max_weight:
        max_weight = ropes[i] * (i + 1)
print(max_weight)