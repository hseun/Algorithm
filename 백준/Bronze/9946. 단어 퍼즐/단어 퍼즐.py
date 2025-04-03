import sys
input = sys.stdin.readline

first = input().strip()
second = input().strip()
case = 1
while True:
	if first == "END" and second == "END":
		break
	if sorted(first) == sorted(second):
		print(f"Case {case}: same")
	else:
		print(f"Case {case}: different")
	case += 1
	first = input().strip()
	second = input().strip()