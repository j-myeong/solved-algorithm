import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    answer = 0
    m, n, k = map(int, input().strip().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]
    spot = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        spot.append((x, y))
        farm[y][x] = 1
    q = deque()
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for x, y in spot:
        if visited[y][x]: continue
        q.append((x, y))
        visited[y][x] = True
        answer += 1
        while q:
            x, y = q.popleft()
            for xi, yi in zip(dx, dy):
                nx, ny = x + xi, y + yi
                if (0 <= nx < m and 0 <= ny < n) and farm[ny][nx] != 0:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((nx, ny))
    print(answer)