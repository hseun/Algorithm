import sys

n = int(sys.stdin.readline())
for i in range(1, n):
    num = [int(a) for a in str(i)]
    num = sum(num)
    if i + num == n:
        sys.stdout.write(str(i))
        sys.exit()
sys.stdout.write("0")
