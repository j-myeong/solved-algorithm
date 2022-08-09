import sys
sys.setrecursionlimit(100000000)

input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    for child in graph[start]:
        if not visited[child]:
            result[child] = start
            dfs(child)

n = int(input())

visited = [False] * (n + 1)
graph = {i:[] for i in range(n + 1)}
result = {i:[] for i in range(n + 1)}

for idx in range(1, n + 1):
    graph[idx] = []

for _ in range(n - 1):
    tmp = input().split(' ')
    parent, child = int(tmp[0]), int(tmp[1])
    graph[parent].append(child)
    graph[child].append(parent)

dfs(1)

for idx in range(2, n + 1):
    print(result[idx])