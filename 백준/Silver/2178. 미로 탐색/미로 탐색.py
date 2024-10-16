import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
visited = [[False] * m for _ in range(n)]
matrix = [[] for _ in range(n)]

for i in range(n):
    for num in input().strip():
        matrix[i].append(int(num))

dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

q = deque()
q.append((0, 0, 1))

while q:
    x, y, value = q.popleft()
    for xi, yi in zip(dx, dy):
        ny = y + yi
        nx = x + xi
        if (0 <= ny < n and 0 <= nx < m) and matrix[ny][nx] != 0 and not visited[ny][nx]:
            matrix[ny][nx] = value + 1
            q.append((nx, ny, value + 1))
            visited[ny][nx] = True

print(matrix[n - 1][m - 1])