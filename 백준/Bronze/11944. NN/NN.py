import sys
input = sys.stdin.readline

n, m = input().split()
m = int(m)
if int(n) * len(n) > m:
    result = n * (m // len(n) + 1)
    print(result[:m])
else:
    result = n * int(n)
    print(result)