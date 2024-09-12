import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = [a for a in range(2, n + 1)]
counts = 0

while counts != k:
    new_nums = []
    for num in nums:
        if num % nums[0] == 0:
            counts += 1
            if counts == k:
                print(num)
                break
        else:
            new_nums.append(num)
    nums = new_nums