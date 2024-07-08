a, b = map(int, input().split())
nums = [1]
count = 2
while len(nums) < b:
    nums += [count] * count
    count += 1
print(sum(nums[a - 1:b]))