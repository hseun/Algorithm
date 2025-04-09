from bisect import bisect_left
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    result = 0
    input()
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    for i in a:
        result += bisect_left(b, i)
    print(result)