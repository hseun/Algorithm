import sys
input = sys.stdin.readline

n = int(input())
trees = sorted(map(int, input().split()), reverse=True)
date = [trees[i] - n + i for i in range(n)]
print(n + max(date) + 2)