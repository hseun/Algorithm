import sys
input = sys.stdin.readline

b, c, d = map(int, input().split())
burgers = sorted(map(int, input().split()), reverse=True)
sides = sorted(map(int, input().split()), reverse=True)
drinks = sorted(map(int, input().split()), reverse=True)
set_count = min(b, c, d)
set_total = [burgers[i] + sides[i] + drinks[i] for i in range(set_count)]
remain_total = sum(burgers[set_count:]) + sum(sides[set_count:]) + sum(drinks[set_count:])
print(sum(set_total) + remain_total)
print(sum([int(price * 0.9) for price in set_total]) + remain_total)