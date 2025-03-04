import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [[0] * n]
table += [[0] + list(map(int, input().split())) for _ in range(n)]
sum_table = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_table[i][j] = table[i][j]
        sum_table[i][j] += sum_table[i][j - 1] + sum_table[i - 1][j]
        sum_table[i][j] -= sum_table[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum_table[x2][y2]
    result -= sum_table[x2][y1 - 1]
    result -= sum_table[x1 - 1][y2]
    result += sum_table[x1 - 1][y1 - 1]
    print(result)
