from collections import deque

n = int(input())

tmp = input().split(' ')

for idx in range(n):
    tmp[idx] = int(tmp[idx])

circle = deque([i for i in range(1, n + 1)])

while len(circle) > 0:
    idx = circle.popleft()
    rt = tmp[idx - 1]
    circle.rotate(-rt if rt < 0 else -rt + 1)
    print(idx, end=' ')