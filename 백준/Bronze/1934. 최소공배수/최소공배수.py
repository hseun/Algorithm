import math

t = int(input())
for _ in range(t):
    num1, num2 = map(int, input().split())
    print(math.lcm(num1, num2))