import sys
input = sys.stdin.readline

n = int(input())
load = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_price = min(prices[:-1])
price = prices[0]
result = 0

for i in range(n - 1):
    if price == min_price:
        result += price * sum(load[i:])
        break
    if price > prices[i]:
        price = prices[i]
    result += price * load[i]
print(result)