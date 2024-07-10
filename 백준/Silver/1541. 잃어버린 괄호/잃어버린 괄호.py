nums = input().split('-')
for i in range(len(nums)):
    if '+' in nums[i]:
        nums[i] = sum(list(map(int, nums[i].split('+'))))
    else:
        nums[i] = int(nums[i])
nums = [-nums[i] if i != 0 else nums[i] for i in range(len(nums))]
print(sum(nums))