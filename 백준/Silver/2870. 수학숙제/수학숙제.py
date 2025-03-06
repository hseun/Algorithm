import sys
import re
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
nums = []
for i in range(n):
    nums += re.sub(r"\D", " ", words[i]).split()
nums = sorted(list(map(int, nums)))
[print(num) for num in nums]