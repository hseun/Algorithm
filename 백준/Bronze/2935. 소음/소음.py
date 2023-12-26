import sys

a = int(sys.stdin.readline())
c = sys.stdin.readline()
b = int(sys.stdin.readline())
if c.find("+") != -1:
    print(a + b)
else:
    print(a * b)