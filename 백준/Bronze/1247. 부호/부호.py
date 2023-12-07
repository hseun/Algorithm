import sys

for _ in range(3):
    result = 0
    n = int(sys.stdin.readline())
    for _ in range(n):
        temp = int(sys.stdin.readline())
        result += temp
    if result == 0: print("0")
    elif result > 0: print("+")
    else: print("-")