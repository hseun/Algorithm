import sys

n, m = map(int, sys.stdin.readline().split())
no_hear = set()
for _ in range(n):
    no_hear.add(sys.stdin.readline())
no_see = set()
for _ in range(m):
    no_see.add(sys.stdin.readline())
no_hear_see = no_hear.intersection(no_see)
no_hear_see = sorted(no_hear_see)
print(len(no_hear_see))
for name in no_hear_see:
    sys.stdout.write(name)