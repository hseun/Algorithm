a, b = map(int, input().split())
if a > b:
    print((a - b + 1) * (a + b) // 2)
else:
    print((b - a + 1) * (a + b) // 2)