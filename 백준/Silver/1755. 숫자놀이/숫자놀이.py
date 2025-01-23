import sys
input = sys.stdin.readline

nums_eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def num_to_eng(num):
    num = [nums_eng[int(i)] for i in list(str(num))]
    return ' '.join(num)

def eng_to_num(eng):
    eng = [str(nums_eng.index(e)) for e in eng.split()]
    return ''.join(eng)

m, n = map(int, input().split())
nums = sorted([num_to_eng(i) for i in range(m, n + 1)])
nums = [eng_to_num(e) for e in nums]

for i in range(len(nums)):
    if i % 10 == 0 and i != 0:
        print()
    print(nums[i], end=' ')