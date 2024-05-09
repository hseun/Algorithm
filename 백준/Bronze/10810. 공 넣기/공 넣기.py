n, m = map(int, input().split())
bag = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    bag[i - 1:j] = [k] * (j - i + 1)
print(' '.join(map(str, bag)))