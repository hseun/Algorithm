from collections import Counter
import sys
input = sys.stdin.readline

input()
nums = list(map(int, input().split()))
nums_count = Counter(nums)
nums_sort = sorted(nums_count, key=lambda x: (-nums_count[x], nums.index(x)))
for num in nums_sort:
    print(*([num] * nums_count[num]), end=" ")