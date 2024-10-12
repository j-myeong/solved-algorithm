from collections import deque

n, m = map(int, input().split())
map_arr = []
visited = []
answer = []

queue = deque([])
# make a map
for row in range(n):
    map_arr.append([])
    visited.append([False] * m)
    answer.append([-1] * m)
    for col, x in enumerate(list(map(int, input().split()))):
        if x == 2:
            queue.append((row, col, 0))
            visited[row][col] = True
            answer[row][col] = 0
        elif x == 0:
            answer[row][col] = 0
        map_arr[row].append(x)

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
while queue:
    row, col, value = queue.popleft()
    for xi, yi in zip(dx, dy):
        nx = col + xi
        ny = row + yi
        if (0 <= nx < m and 0 <= ny < n) and map_arr[ny][nx] != 0:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, value + 1))
                answer[ny][nx] = value + 1

for line in answer:
    print(*line)