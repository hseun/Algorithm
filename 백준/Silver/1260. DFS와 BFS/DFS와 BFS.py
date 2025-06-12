from collections import  deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

def dfs(start, visited):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(node, visited)
    return visited

def bfs(start):
    que = deque([start])
    visited = []
    visited.append(start)

    while que:
        current = que.popleft()
        for next_node in graph[current]:
            if next_node not in visited:
                visited.append(next_node)
                que.append(next_node)
    return visited

print(*dfs(v, []))
print(*bfs(v))