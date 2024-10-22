x, y = map(int, input().split())
arr = [y]
answer = -1
while y >= x:
    if y % 2 == 0:
        y //= 2
    else:
        if str(y)[-1] != '1': break
        tmp = str(y)[:-1]
        y = int(tmp or 0)
    arr.append(y)

for idx, i in enumerate(arr):
    if i == x:
        answer = idx + 1
        break

print(answer)