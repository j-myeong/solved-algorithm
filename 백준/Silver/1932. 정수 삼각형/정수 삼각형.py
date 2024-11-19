n = int(input())
arr = [[] for _ in range(n)]

for line in range(n):
    if line == 0:
        arr[0].append(int(input()))
        continue
    elif line == 1:
        x, y = map(int, input().split())
        arr[1].append(x + arr[0][0])
        arr[1].append(y + arr[0][0])
        continue
    for idx, num in enumerate(list(map(int, input().split()))):
        if idx == 0:
            arr[line].append(arr[line - 1][0] + num)
        elif idx == line:
            arr[line].append(arr[line - 1][-1] + num)
        else:
            arr[line].append(max(arr[line - 1][idx - 1], arr[line - 1][idx]) + num)

print(max(arr[-1]))
