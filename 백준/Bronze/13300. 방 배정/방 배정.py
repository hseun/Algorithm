import sys
input = sys.stdin.readline

n, k = map(int, input().split())
girl = [0] * 6
boy = [0] * 6
for _ in range(n):
    s, y = map(int, input().split())
    if s:
        boy[y - 1] += 1
    else:
        girl[y - 1] += 1
        
room = 0
for i in range(6):
    room += girl[i] // k + girl[i] % k
    room += boy[i] // k + boy[i] % k
print(room)