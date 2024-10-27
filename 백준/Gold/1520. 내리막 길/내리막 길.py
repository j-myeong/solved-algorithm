import sys

sys.setrecursionlimit(999999)

def recur(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    point = 0
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for xi, yi in zip(dx, dy):
        nx = x + xi
        ny = y + yi

        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] < graph[y][x]:
                point += recur(nx, ny)
    dp[y][x] = point
    return dp[y][x]


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]

answer = recur(0, 0)
print(answer)