import sys
input = sys.stdin.readline

students = [list(reversed(input().strip())) for _ in range(int(input()))]
student_set = set()
k = 1
while True:
    for student in students:
        student_set.add(''.join(student[:k]))
    if len(students) == len(student_set):
        break
    k += 1
    student_set.clear()
print(k)