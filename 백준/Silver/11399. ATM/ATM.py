import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
times = sorted(list(map(int, input().split())))
t = 0

for i in range(1, n + 1):
    t += sum(times[:i])

print(str(t))