import sys
input = sys.stdin.readline

people = [input().strip() for _ in range(int(input()))]
if sorted(people) == people:
	print("INCREASING")
elif sorted(people, reverse=True) == people:
	print("DECREASING")
else:
	print("NEITHER")