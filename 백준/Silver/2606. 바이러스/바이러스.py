import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return sum(visited) - 1

n = int(input())
m = int(input())

computers = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    computers[a] += [b]
    computers[b] += [a]

print(bfs(computers, 1, visited))