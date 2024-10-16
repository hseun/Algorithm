import sys
input = sys.stdin.readline

int(input())
nums = list(map(int, input().split()))
x = int(input())

counter = 0
num_set = set(nums)

for num in nums:
    if x - num in num_set:
        counter += 1
print(counter // 2)