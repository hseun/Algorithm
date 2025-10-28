import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1
print(count)