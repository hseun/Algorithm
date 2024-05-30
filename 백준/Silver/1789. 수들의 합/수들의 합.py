s = int(input()) - 1
n = 1
while s > 0 and s - n > 0:
    n += 1
    s -= n
print(n)