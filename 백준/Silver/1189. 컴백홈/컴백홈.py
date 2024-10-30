def recur(row, col, count):
    global answer

    if graph[row][col] == 2 and count == k:
        answer += 1
        return

    for xi, yi in zip(dx, dy):
        nrow = row + yi
        ncol = col + xi
        ncount = count + 1

        if 0 <= nrow < r and 0 <= ncol < c and graph[nrow][ncol] != -1:
            if not visited[nrow][ncol]:
                visited[nrow][ncol] = True
                recur(nrow, ncol, ncount)
                visited[nrow][ncol] = False

import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = [[0 for _ in range(c)] for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
answer = 0
for row in range(r):
    for col, item in enumerate(list(input())):
        if item == "T":
            graph[row][col] = -1


graph[0][c - 1] = 2
visited[r - 1][0] = True

dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

recur(r - 1, 0, 1)
print(answer)