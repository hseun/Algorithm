import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
student = input().split()
wanted = [*student]
for _ in range(n):
    wanted.extend(input().split())
wanted_count = Counter(wanted)
wanted_count = sorted(wanted_count.items(), key=lambda x: (-x[1], x[0]))
for name, count in wanted_count:
    print(name, count - 1)