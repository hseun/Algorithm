import sys

m = int(input())
n = int(input())
li = [a for a in range(2, n + 1)]
sosu = []
if len(li) == 0:
    print("-1")
    sys.exit()
while li[0] ** 2 <= n:
    if li[0] >= m:
        sosu.append(li[0])
    li = [a for a in li if a % li[0] != 0]
li = [a for a in li if a >= m]
sosu.extend(li)
if len(sosu) == 0:
    print("-1")
else:
    Sum = 0
    for i in sosu:
        Sum += i
    print(Sum)
    print(sosu[0])