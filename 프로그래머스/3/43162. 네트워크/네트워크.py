from collections import deque


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:
                graph[i].append(j)
    q = deque()
    visited = [False] * n
    for i in range(n):
        if not visited[i]: 
            answer += 1
            q.append(i)
        while q:
            idx = q.popleft()
            for item in graph[idx]:
                if not visited[item]:
                    q.append(item)
                    visited[item] = True
    return answer