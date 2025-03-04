import sys
input = sys.stdin.readline

def total_sum(arr):
    sum_arr = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sum_arr[i][j] = arr[i][j]
            sum_arr[i][j] += sum_arr[i][j - 1] + sum_arr[i - 1][j]
            sum_arr[i][j] -= sum_arr[i - 1][j - 1]
    return sum_arr

def section_sum(sum_arr, i1, j1, i2, j2):
    result = sum_arr[i2][j2]
    result -= sum_arr[i2][j1 - 1]
    result -= sum_arr[i1 - 1][j2]
    result += sum_arr[i1 - 1][j1 - 1]
    return result

n, m = map(int, input().split())
table = [[0] * n]
table += [[0] + list(map(int, input().split())) for _ in range(n)]
sum_table = total_sum(table)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(section_sum(sum_table, x1, y1, x2, y2))