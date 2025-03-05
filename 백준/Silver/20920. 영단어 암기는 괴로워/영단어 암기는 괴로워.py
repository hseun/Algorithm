import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().strip() for _ in range(n)]
words = [word for word in words if len(word) >= m]
words_counter = sorted(Counter(words).items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
[print(word[0]) for word in words_counter]