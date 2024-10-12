import copy
from collections import deque

n, m = map(int, input().split())
matrix = []
gas = []
ret = 0

def bfs():
    global ret
    visited = [[False] * m for _ in range(n)]
    q = deque(gas)
    copied = copy.deepcopy(matrix)
    count = 0
    dy, dx = (1, -1, 0, 0), (0, 0, -1, 1)

    while q:
        y, x = q.popleft()
        copied[y][x] = 2
        for xi, yi in zip(dx, dy):
            nx = x + xi
            ny = y + yi
            if (0 <= nx < m and 0 <= ny < n) and not visited[ny][nx]:
                if copied[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))


    for line in copied:
        for item in line:
            if item == 0:
                count += 1
    if ret < count:
        ret = count

def dfs(count, sy, sx):
    if count >= 3:
        bfs()
        return
    for ny in range(sy, n):
        for nx in range(sx, m):
            if matrix[ny][nx] == 0:
                matrix[ny][nx] = 1
                dfs(count + 1, ny, nx)
                matrix[ny][nx] = 0
        sx = 0

for y in range(n):
    matrix.append([])
    for x, node in enumerate(list(map(int, input().split()))):
        if node == 2: # gas
            gas.append((y, x))
        matrix[y].append(node)
dfs(0, 0, 0)
print(ret)