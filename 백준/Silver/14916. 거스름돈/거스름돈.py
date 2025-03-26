import sys
input = sys.stdin.readline

money = int(input())
cnt = 0
while True:
    if money % 5 == 0:
        cnt += money // 5
        break
    else:
        money -= 2
        cnt += 1
    if money < 0:
        cnt -= 1
        break
print(-1 if money < 0 else cnt)