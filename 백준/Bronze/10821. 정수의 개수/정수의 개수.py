import sys
input = sys.stdin.readline

nums = input().strip().split(',')
result = 0
for num in nums:
    if num.isdigit():
        result += 1
print(result)