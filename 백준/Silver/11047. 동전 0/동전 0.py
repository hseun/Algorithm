import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
result = 0
for coin in reversed(coins):
    result += k // coin
    k = k % coin
print(result)