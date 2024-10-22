import sys
input = sys.stdin.readline

for _ in range(int(input())):
    max_count = 0
    max_school = ""
    for _ in range(int(input())):
        school, drink = input().split()
        drink = int(drink)
        if drink > max_count:
            max_count = drink
            max_school = school
    print(max_school)