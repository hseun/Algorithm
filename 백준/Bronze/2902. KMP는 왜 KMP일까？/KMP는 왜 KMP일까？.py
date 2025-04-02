import sys
input = sys.stdin.readline

long_name = input().strip().split('-')
short_name = []
for name in long_name:
    short_name.append(name[0])
print(''.join(short_name))