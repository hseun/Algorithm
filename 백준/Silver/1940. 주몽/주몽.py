import sys
input = sys.stdin.readline

left = 0
right = int(input()) - 1
m = int(input())
nums = sorted(list(map(int, input().split())))
result = 0

while left < right:
    n = nums[left] + nums[right]
    if n == m:
        result += 1
        left += 1
        right -= 1
    elif n > m:
        right -= 1
    else:
        left += 1
print(result)