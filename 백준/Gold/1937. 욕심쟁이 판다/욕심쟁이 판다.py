import sys

sys.setrecursionlimit(999999)

def recur(x, y):
    if dp[y][x] != 0:
        return dp[y][x]

    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for xi, yi in zip(dx, dy):
        nx = x + xi
        ny = y + yi

        if 0 <= nx < n and 0 <= ny < n:
            if graph[ny][nx] > graph[y][x]:
                dp[y][x] = max(dp[y][x], recur(nx, ny) + 1)

    return dp[y][x]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        recur(x, y)

print(max(map(max, dp)) + 1)