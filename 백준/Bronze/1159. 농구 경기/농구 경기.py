from collections import Counter
import sys
input = sys.stdin.readline

names = Counter([input()[0] for _ in range(int(input()))])
names = sorted(filter(lambda x: names[x] >= 5, names))
print(''.join(names) if len(names) else "PREDAJA")