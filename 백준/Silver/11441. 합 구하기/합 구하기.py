import sys

input = sys.stdin.readline

n = int(input())
a = input().split(' ')

a[0] = int(a[0])

for idx in range(1, n):
    a[idx] = int(a[idx])
    a[idx] += a[idx - 1]
a.append(0)
test = int(input())

for _ in range(test):
    tmp = input().split(' ')
    i, j = int(tmp[0]), int(tmp[1])
    print(a[j - 1] - a[i - 2])