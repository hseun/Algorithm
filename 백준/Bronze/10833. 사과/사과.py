import sys
input = sys.stdin.readline

apple_sum = 0
for _ in range(int(input())):
    student, apple = map(int, input().split())
    apple_sum += apple % student
print(apple_sum)