first = [0, 500, 300, 300, 200, 200, 200] + [50] * 4 + [30] * 5 + [10] * 6
second = [0, 512, 256, 256] + [128] * 4 + [64] * 8 + [32] * 16

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a >= len(first): a = 0
    if b >= len(second): b = 0
    print((first[a] + second[b]) * 10000)