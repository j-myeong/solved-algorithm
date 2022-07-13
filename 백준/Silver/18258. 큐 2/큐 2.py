from collections import deque
import sys

input = sys.stdin.readline

test = int(input())

data = deque()

for _ in range(test):
    line = input().strip().split(' ')
    if line[0] == 'push':
        data.append(int(line[1]))
    elif line[0] == 'pop':
        print(data.popleft() if data else -1)
    elif line[0] == 'size':
        print(len(data))
    elif line[0] == 'empty':
        print(0 if data else 1)
    elif line[0] == 'front':
        print(data[0] if data else -1)
    elif line[0] == 'back':
        print(data[-1] if data else -1)