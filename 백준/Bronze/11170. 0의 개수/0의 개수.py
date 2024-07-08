t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(''.join(map(str, [a for a in range(n, m + 1)])).count('0'))