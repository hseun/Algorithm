import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
files = [input().split(".")[1].strip() for _ in range(n)]
count = Counter(files)
for file in sorted(count):
    print(file, count[file])