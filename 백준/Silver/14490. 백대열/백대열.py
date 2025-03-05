import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split(":"))
gcd = math.gcd(n, m)
print(f"{n // gcd}:{m // gcd}")