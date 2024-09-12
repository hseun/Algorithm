import sys
input = sys.stdin.readline

counts = 0

while True:
    counts += 1
    l, p, v = map(int, input().split())
    if v == 0:
        break
    if v % p < l:
        print("Case {}: {}".format(counts, l * (v // p) + v % p))
    else:
        print("Case {}: {}".format(counts, l * (v // p) + l))