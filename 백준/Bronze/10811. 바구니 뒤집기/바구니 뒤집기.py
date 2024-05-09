n, m = map(int, input().split())
bag = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    bag[i - 1:j] = reversed(bag[i - 1:j])
print(' '.join(map(str, bag)))