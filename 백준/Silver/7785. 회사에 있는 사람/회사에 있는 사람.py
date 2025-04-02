import sys
input = sys.stdin.readline

office = set()
for _ in range(int(input())):
    p = input().split()[0]
    if p in office:
        office.discard(p)
    else:
        office.add(p)
[print(p) for p in sorted(office, reverse=True)]