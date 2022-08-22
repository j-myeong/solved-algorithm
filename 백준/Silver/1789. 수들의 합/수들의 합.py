import sys


input = sys.stdin.readline

s = int(input())
result = []

cnt = 1
while s != 0:
    if cnt > s:
        tmp = result.pop()
        s += tmp
        result.append(s)
        break
    result.append(cnt)
    s -= cnt
    cnt += 1

print(len(result))