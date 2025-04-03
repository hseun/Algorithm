import sys
input = sys.stdin.readline

s = input().strip()
while True:
	if s == '#':
		break
	s = s.split()
	alpha = s.pop(0)
	print(alpha, ''.join(s).lower().count(alpha))
	s = input().strip()