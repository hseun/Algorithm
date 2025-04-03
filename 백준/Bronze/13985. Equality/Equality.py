import sys
input = sys.stdin.readline

nums = input().split()
print("YES" if int(nums[0]) + int(nums[2]) == int(nums[4]) else "NO")