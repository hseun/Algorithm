import sys
input = sys.stdin.readline

for i in range(int(input())):
    score = sorted(list(map(int, input().split()))[1:])
    score_gap = 0
    for j in range(len(score) - 1):
        if score_gap < score[j + 1] - score[j]:
            score_gap = score[j + 1] - score[j]

    print("Class", i + 1)
    print(f"Max {score[-1]}, Min {score[0]}, Largest gap {score_gap}")