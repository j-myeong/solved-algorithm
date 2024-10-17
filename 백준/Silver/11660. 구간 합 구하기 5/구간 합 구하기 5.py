import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

prefix = [[0] * (n + 1) for _ in range(n + 1)]

for row in range(n):
    for col, item in enumerate(list(map(int, input().strip().split()))):
        prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + item

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().strip().split())
    print(prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1])