x, y = input().split()
x, y = reversed(x), reversed(y)
result = str(int("".join(x)) + int("".join(y)))
print(int("".join(reversed(result))))