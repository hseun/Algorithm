import sys
input = sys.stdin.readline

for _ in range(int(input())):
	candy, box_count = map(int, input().split())
	boxes = []
	for _ in range(box_count):
		a, b = map(int, input().split())
		boxes.append(a * b)
	boxes.sort(reverse=True)
	for i in range(box_count):
		if sum(boxes[:i + 1]) >= candy:
			print(i + 1)
			break