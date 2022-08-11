import sys
sys.setrecursionlimit(10000000)

input = sys.stdin.readline

cnt = 1
def dfs(start):
    global cnt
    result[start] = cnt
    visited[start] = True
    graph[start].sort()
    for child in graph[start]:
        if not visited[child]:
            cnt += 1
            dfs(child)

tmp = input().split(' ')
n, m, r = int(tmp[0]), int(tmp[1]), int(tmp[2])

visited = [False] * (n + 1)
result = [0] * (n + 1)
graph = {x:[] for x in range(n + 1)}

for _ in range(m):
    tmp = input().split(' ')
    u, v = int(tmp[0]), int(tmp[1])
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for i in range(1, n + 1):
    print(result[i])