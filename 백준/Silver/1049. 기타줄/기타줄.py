import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set_price = 1001
one_price = 1001
for _ in range(m):
    s, o = map(int, input().split())
    if s < set_price:
        set_price = s
    if o < one_price:
        one_price = o
if one_price * 6 < set_price:
    print(n * one_price)
elif (n % 6) * one_price > set_price:
    print((n // 6 + 1) * set_price)
else:
    print(((n // 6) * set_price) + ((n % 6) * one_price))