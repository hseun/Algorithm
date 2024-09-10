import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
sum_max = 0

for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if sum_max < cards[i] + cards[j] + cards[k] <= m:
                sum_max = cards[i] + cards[j] + cards[k]
print(sum_max)