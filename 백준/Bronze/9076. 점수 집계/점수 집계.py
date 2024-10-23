import sys
input = sys.stdin.readline

for _ in range(int(input())):
    score = sorted(list(map(int, input().split())))[1:-1]
    if max(score) - min(score) >= 4:
        print("KIN")
    else:
        print(sum(score))