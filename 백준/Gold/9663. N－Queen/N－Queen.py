def recur(row):
    global ans
    if row == n:
        ans += 1
        return
    for i in range(n):
        if not graph[row][i]:
            check(row, i)
            recur(row + 1)
            check(row, i, False)

def check(row, col, value=True):
    for i in range(row, n): # 세로 칠
        graph[i][col] += 1 if value else -1

    if col > 0:
        for i in range(col, -1, -1): #
            if row + col - i >= n: break
            graph[row + col - i][i] += 1 if value else -1

    if col < n - 1:
        for i in range(col, n):
            if row + i - col >= n: break
            graph[row + i - col][i] += 1 if value else -1

    graph[row][col] -= 1 if value else -1

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
ans = 0
recur(0)
print(ans)
