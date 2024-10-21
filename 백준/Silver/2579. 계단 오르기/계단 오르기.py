import sys

sys.setrecursionlimit(99999)

n = int(input())
a = [0] * n
b = [0] * n

for i in range(n):
    if i == 0:
        a[i] = int(input())
    elif i == 1:
        b[i] = int(input())
        a[i] = b[i] + a[i - 1]
    else:
        tmp = int(input())
        a[i] = b[i - 1] + tmp
        b[i] = max(a[i - 2], b[i - 2]) + tmp
print(max(a[-1], b[-1]))