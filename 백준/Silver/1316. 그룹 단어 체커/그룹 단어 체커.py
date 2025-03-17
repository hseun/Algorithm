import sys
import re
from itertools import count

input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    word = input().strip()
    alpha = set(word)
    counts = len(alpha)
    for w in alpha:
        first_index = word.index(w)
        last_index = word.rindex(w)
        if first_index == last_index:
            counts -= 1
            continue
        r = re.sub(w, "", word[first_index:last_index + 1])
        if len(r) > 0: break
        counts -= 1
    if counts == 0:
        result += 1
print(result)