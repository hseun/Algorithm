li = [a for a in range(2, 1001)]
sosu = []
while li[0] ** 2 <= 1000:
    sosu.append(li[0])
    li = [a for a in li if a % li[0] != 0]
sosu.extend(li)

count = 0
n = int(input())
num = list(map(int, input().split()))
for i in num:
    if i in sosu:
        count += 1
print(count)