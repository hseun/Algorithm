import sys

input = sys.stdin.readline

for i in range(int(input())):
    print(f"Case #{i + 1}:", *list(reversed(input().strip().split())))