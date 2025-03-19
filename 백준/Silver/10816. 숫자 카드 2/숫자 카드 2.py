import sys
from collections import Counter

input = sys.stdin.readline

input()
cards = Counter(map(int, input().split()))
input()
find_want = list(map(int, input().split()))
for want in find_want:
    counts = cards.get(want)
    print(counts if counts else 0, end=" ")