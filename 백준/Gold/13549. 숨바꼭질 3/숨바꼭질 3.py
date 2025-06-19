from collections import deque
import sys
input = sys.stdin.readline

start, target = map(int, input().split())
que = deque()
MAX = 100001
visited = [False] * MAX

que.append((start, 0))
visited[start] = True
min_time = MAX

while que:
    current, time = que.popleft()

    if current == target:
        min_time = min(min_time, time)

    if 0 <= current * 2 <= MAX and not visited[current * 2]:
        visited[current * 2] = True
        que.append((current * 2, time))
    if 0 <= current - 1 < MAX and not visited[current - 1]:
        visited[current - 1] = True
        que.append((current - 1, time + 1))
    if 0 <= current + 1 < MAX and not visited[current + 1]:
        visited[current + 1] = True
        que.append((current + 1, time + 1))
print(min_time)