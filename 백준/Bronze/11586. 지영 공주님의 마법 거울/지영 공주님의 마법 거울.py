import sys
input = sys.stdin.readline

n = int(input())
princess = [input().strip() for _ in range(n)]
mind = int(input())

if mind == 1:
    for p in princess:
        print(p)
elif mind == 2:
    for p in princess:
        print(''.join(list(reversed(p))))
else:
    for i in range(n - 1, -1, -1):
        print(princess[i])