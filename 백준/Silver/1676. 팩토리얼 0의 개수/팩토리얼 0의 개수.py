import math

n = int(input())
num = str(math.factorial(n))
count = 0
for i in range(len(num) - 1, 0, -1):
    if num[i] != '0':
        break
    else:
        count += 1
print(count)