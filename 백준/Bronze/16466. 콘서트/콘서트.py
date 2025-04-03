import sys
input = sys.stdin.readline

input()
ticket = set(map(int, input().split()))
n = 1
while True:
	if n not in ticket:
		print(n)
		break
	n += 1