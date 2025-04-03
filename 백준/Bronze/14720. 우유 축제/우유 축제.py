import sys
input = sys.stdin.readline

input()
milks = list(map(int, input().split()))
result = 0
want_milk = 0
for milk in milks:
	if milk == want_milk:
		result += 1
		want_milk = (want_milk + 1) % 3
print(result)