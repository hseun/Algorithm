import sys
input = sys.stdin.readline

num = list(map(int, list(input().strip())))
half_len = len(num) // 2
print("LUCKY" if sum(num[:half_len]) == sum(num[half_len:]) else "READY")