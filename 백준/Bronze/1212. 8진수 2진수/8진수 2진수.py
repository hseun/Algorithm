import sys
input = sys.stdin.readline

n = f"0o{input().strip()}"
n = str(bin(int(n, 8)))
print(n[2:])