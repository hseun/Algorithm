import re
import sys
input = sys.stdin.readline

a, b = input().strip().split()
max_a = int(re.sub("5", "6", a))
max_b = int(re.sub("5", "6", b))
min_a = int(re.sub("6", "5", a))
min_b = int(re.sub("6", "5", b))
print(min_a + min_b, max_a + max_b)