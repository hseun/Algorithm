import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set([input() for _ in range(n)])
checking_s = [input() for _ in range(m)]
print(len([check for check in checking_s if check in s]))