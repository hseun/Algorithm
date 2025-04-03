import sys
input = sys.stdin.readline

n = "0x" + input().strip()
print(int(n, 16))