import sys
input = sys.stdin.readline

test = int(input())

data = []

for _ in range(test):
    line = input().strip().split(' ')
    if line[0] == 'push':
        data.append(int(line[1]))
    elif line[0] == 'pop':
        print(data.pop() if data else -1)
    elif line[0] == 'size':
        print(len(data))
    elif line[0] == 'empty':
        print(0 if data else 1)
    elif line[0] == 'top':
        print(data[-1] if data else -1)