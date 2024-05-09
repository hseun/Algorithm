n, m = map(int, input().split())
bag = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    bag[i - 1], bag[j - 1] = bag[j - 1], bag[i - 1]
print(' '.join(map(str, bag)))