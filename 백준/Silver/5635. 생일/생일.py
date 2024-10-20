import sys
input = sys.stdin.readline

students = []
for _ in range(int(input())):
    student = input().split()
    students.append((student[0], int(student[1]), int(student[2]), int(student[3])))
students = sorted(students, key=lambda x: (x[3], x[2], x[1]))

print(students[-1][0])
print(students[0][0])