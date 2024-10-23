import sys
input = sys.stdin.readline

input()
a_set = set(list(map(int, input().split())))
b_set = set(list(map(int, input().split())))
result = sorted(list(a_set - b_set))
print(len(result))
print(*result)