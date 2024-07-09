import statistics

nums = [int(input()) for _ in range(10)]
print(sum(nums) // len(nums))
print(statistics.mode(nums))