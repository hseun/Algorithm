import sys
input = sys.stdin.readline

x = input().strip()
if x.startswith('0x'):
    x = int(x, 16)
elif x.startswith('0'):
    x = int(x, 8)
print(x)