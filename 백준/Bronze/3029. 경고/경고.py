import sys
input = sys.stdin.readline

def calculate_time(now, target):
	if now == target:
		return 24, 0, 0
	second = int(target[2]) - int(now[2])
	minute = int(target[1]) - int(now[1])
	hour = int(target[0]) - int(now[0])
	if second < 0:
		second += 60
		minute -= 1
	if minute < 0:
		minute += 60
		hour -= 1
	if hour < 0:
		hour += 24
	return hour, minute, second

now = input().strip().split(':')
target = input().strip().split(':')
hour, minute, second = calculate_time(now, target)
print("%02d:%02d:%02d" % (hour, minute, second))