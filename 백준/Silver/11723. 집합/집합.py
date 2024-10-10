import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    input_op = input().split()
    op = input_op[0]
    param = int(input_op[1]) if len(input_op) > 1 else None
    if op == 'add':
        s.add(param)
    elif op == 'remove':
        if param in s:
            s.remove(param)
    elif op == 'check':
        print(int(param in s))
    elif op == 'toggle':
        if param in s:
            s.remove(param)
        else:
            s.add(param)
    elif op == 'all':
        s = set([i for i in range(1, 21)])
    elif op == 'empty':
        s = set()
