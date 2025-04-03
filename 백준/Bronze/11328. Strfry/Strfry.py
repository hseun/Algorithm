import sys
input = sys.stdin.readline

for _ in range(int(input())):
    first, second = input().strip().split()
    print("Possible" if sorted(first) == sorted(second) else "Impossible")