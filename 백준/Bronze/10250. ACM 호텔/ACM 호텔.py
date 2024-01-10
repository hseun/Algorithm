t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n > h:
        if n % h == 0:
            y = 100 * h
            x = n // h
        else:
            y = 100 * (n % h)
            x = 1 + (n // h)
    elif n == h:
        y = 100 * n
        x = n // h
    else:
        y = 100 * n
        x = 1
    print(y + x)