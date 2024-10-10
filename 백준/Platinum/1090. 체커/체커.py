n = int(input())
map_arr = []
x_arr = []
y_arr = []
answer = [-1] * n
for _ in range(n):
    x, y = map(int, input().split())
    map_arr.append([x, y])
    x_arr.append(x)
    y_arr.append(y)

for x in x_arr:
    for y in y_arr:
        dist = []
        for ex, ey in map_arr:
            d = abs(ex-x) + abs(ey-y)
            dist.append(d)

        dist.sort()

        tmp = 0
        for i in range(len(dist)):
            d = dist[i]
            tmp += d
            if answer[i] == -1:
                answer[i] = tmp
            else:
                answer[i] = min(answer[i], tmp)
print(*answer)

