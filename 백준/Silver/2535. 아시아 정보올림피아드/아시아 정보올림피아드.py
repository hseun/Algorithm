import sys
from collections import Counter
input = sys.stdin.readline

students = []
result_country = Counter()
result = []
for _ in range(int(input())):
    country, name, score = map(int, input().split())
    students.append((country, name, score))
students = sorted(students, key=lambda x: -x[2])
for student in students:
    if len(result) >= 3:
        break
    if result_country[student[0]] >= 2:
        continue
    result_country[student[0]] += 1
    result.append((student[0], student[1]))
for student in result:
    print(*student)