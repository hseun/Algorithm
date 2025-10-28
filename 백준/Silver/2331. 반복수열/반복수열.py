import sys

input = sys.stdin.readline

a, p = map(int, input().split())
visited_num = set()

nums = [a]
visited_num.add(a)

while True:
    num = str(nums[-1])
    next_num = sum([int(n) ** p for n in num])
    if next_num in visited_num:
        find_index = nums.index(next_num)
        print(find_index)
        break
    visited_num.add(next_num)
    nums.append(next_num)