import math

n = int(input())
a = math.log(n, 2)
if not a - int(a):
    print(1)
else:
    print(0)