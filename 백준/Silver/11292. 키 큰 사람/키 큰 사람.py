import sys
input = sys.stdin.readline

n = int(input())
while True:
	if n == 0:
		break
	people = []
	max_tall = 0
	for i in range(n):
		name, tall = input().strip().split()
		tall = float(tall)
		if tall > max_tall:
			people = [name]
			max_tall = tall
		elif tall == max_tall:
			people.append(name)
	print(*people)
	n = int(input())