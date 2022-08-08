from collections import deque
import sys


def dfs(start, visited = []):
    visited.append(start)
    for child in graph[start]:
        if child not in visited:
            visited = dfs(child, visited)
    return visited

def bfs(start):
    visited = [start]
    deq = deque()
    deq.append(start)
    while deq:
        v = deq.popleft()
        for child in graph[v]:
            if child not in visited:
                visited.append(child)
                deq.append(child)
    return visited

input = sys.stdin.readline

tmp = input().split(' ')

n, m, v = int(tmp[0]), int(tmp[1]), int(tmp[2])

graph = {}

for idx in range(1, n + 1):
    graph[idx] = []

for _ in range(m):
    tmp = input().split(' ')
    x, y = int(tmp[0]), int(tmp[1])
    graph[y].append(x)
    graph[x].append(y)

for node in graph:
    graph[node].sort()

print(" ".join(map(str, dfs(v))))
print(" ".join(map(str, bfs(v))))

