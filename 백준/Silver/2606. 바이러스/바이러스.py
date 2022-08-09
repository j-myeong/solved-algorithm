import sys

input = sys.stdin.readline

cnt = 0
def dfs(start):
    global cnt
    visited[start] = True
    for child in graph[start]:
        if not visited[child]:
            cnt += 1
            dfs(child)

n = int(input())

visited = [False] * (n + 1)
graph = {x:[] for x in range(n + 1)}

test = int(input())

for _ in range(test):
    tmp = input().split(' ')
    x, y = int(tmp[0]), int(tmp[1])
    graph[x].append(y)
    graph[y].append(x)

dfs(1)

print(cnt)