from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

print(round(sum(nums) / n))
print(sorted(nums)[n // 2])

c = sorted(Counter(nums).items(), key=lambda pair: (-pair[1], pair[0]))
if len(c) > 1 and c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])

print(max(nums) - min(nums))