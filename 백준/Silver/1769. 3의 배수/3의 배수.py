import sys
input = sys.stdin.readline

n = list(input().strip())
counts = 0

while len(n) > 1:
    n = list(str(sum([int(num) for num in n])))
    counts += 1
print(counts)
if int(n[0]) % 3 == 0:
    print("YES")
else:
    print("NO")