from collections import deque

tmp = input().split()

n = int(tmp[0])
k = int(tmp[1])

circle = deque([i for i in range(1, n+1)])

print('<', end='')
while len(circle) > 1:
    circle.rotate(-k + 1)
    print(circle.popleft(), end=', ')
print(circle.pop(), end='')
print('>')