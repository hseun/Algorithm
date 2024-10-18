import sys
input = sys.stdin.readline

scores = [int(input()) for _ in range(8)]
result_score = set(sorted(scores, reverse=True)[:5])

print(sum(result_score))
for i in range(8):
    if scores[i] in result_score:
        print(i + 1, end=" ")