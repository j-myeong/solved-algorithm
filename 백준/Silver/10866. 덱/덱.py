from collections import deque
import sys

input = sys.stdin.readline

test = int(input())

data = deque()

for _ in range(test):
    line = input().strip().split(' ')
    if line[0] == 'push_back':
        data.append(int(line[1]))
    elif line[0] == 'push_front':
        data.appendleft(int(line[1]))
    elif line[0] == 'pop_back':
        print(data.pop() if data else -1)
    elif line[0] == 'pop_front':
        print(data.popleft() if data else -1)
    elif line[0] == 'size':
        print(len(data))
    elif line[0] == 'empty':
        print(0 if data else 1)
    elif line[0] == 'front':
        print(data[0] if data else -1)
    elif line[0] == 'back':
        print(data[-1] if data else -1)