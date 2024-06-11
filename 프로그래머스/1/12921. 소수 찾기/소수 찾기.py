def solution(n):
    nums = [a for a in range(2, n + 1)]
    answer = []
    while n ** (1 / 2) >= nums[0]:
        answer.append(nums[0])
        nums = [a for a in nums if a % nums[0] != 0]
    answer.extend(nums)
    return len(answer)