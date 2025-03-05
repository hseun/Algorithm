import sys
input = sys.stdin.readline

def str_to_int(s):
    num = list(s)
    num = [int(a) for a in num if a.isdigit()]
    return sum(num)

n = int(input())
serials = sorted([input().strip() for _ in range(n)], key=lambda x: (len(x), str_to_int(x), x))
[print(serial) for serial in serials]