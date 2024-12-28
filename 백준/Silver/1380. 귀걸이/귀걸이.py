import sys
input = sys.stdin.readline

counts = 0
while True:
    n = int(input())
    if n == 0: break
    counts += 1
    girls = [input().strip() for _ in range(n)]
    earring = [False] * n
    for _ in range(2 * n - 1):
        num = int(input().split()[0]) - 1
        earring[num] = not earring[num]
    print(counts, girls[earring.index(True)])