from collections import deque

n = int(input())
cq = deque([i for i in range(1, n + 1)])

while len(cq) > 1:
    cq.popleft()
    cq.rotate(-1)

print(cq.pop())