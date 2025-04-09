import sys
input = sys.stdin.readline

n, l = map(int ,input().split())
h = sorted(map(int, input().split()), reverse=True)
while len(h) > 0 and h[-1] <= l:
    l += 1
    h.pop()
print(l)