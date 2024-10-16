import sys
input = sys.stdin.readline

input()
nums = sorted(list(set(map(int, input().split()))))
[print(num, end=' ') for num in nums]