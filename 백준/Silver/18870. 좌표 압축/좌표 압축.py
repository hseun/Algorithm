import sys

input = sys.stdin.readline

n = int(input())
x_list = list(map(int, input().split()))
x_set = sorted(set(x_list))
index_map = {value: index for index, value in enumerate(x_set)}
print(' '.join(map(str, [index_map[x] for x in x_list])))