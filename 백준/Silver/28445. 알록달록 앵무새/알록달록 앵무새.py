import sys
input = sys.stdin.readline

parents = set()
for _ in range(2):
    [parents.add(a) for a in input().split()]
results = []
for p1 in parents:
    for p2 in parents:
        results.append(f"{p1} {p2}")
results = sorted(results)
[print(result) for result in results]