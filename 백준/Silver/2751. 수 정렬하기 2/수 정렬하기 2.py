import sys

num = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
num.sort()
for i in num:
    sys.stdout.write(str(i) + "\n")