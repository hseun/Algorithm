import sys
input = sys.stdin.readline

k_score = sorted([int(input()) for _ in range(10)], reverse=True)
w_score = sorted([int(input()) for _ in range(10)], reverse=True)
print(sum(k_score[:3]), sum(w_score[:3]))