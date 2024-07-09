a, b = input().split()
a = sum([int(i) for i in list(a)])
b = [int(i) for i in list(b)]
result = 0
for i in b:
    result += a * i
print(result)