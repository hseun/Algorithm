import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque()
for i in range(1, n + 1):
    card.append(i)
while len(card) > 1:
    del card[0]
    a = card.popleft()
    card.append(a)
sys.stdout.write(str(card[0]))