import sys
input = sys.stdin.readline

nums = sorted([int(input()) for _ in range(int(input()))], reverse=True)
[print(num) for num in nums]