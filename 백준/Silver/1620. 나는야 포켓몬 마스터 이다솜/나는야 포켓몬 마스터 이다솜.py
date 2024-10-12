n, m = map(int, input().split())
d = {}
arr = ["",]
for i in range(1, n+1):
    name = input()
    arr.append(name)
    d[name] = i

for _ in range(m):
    tmp = input()
    if tmp.isnumeric():
        print(arr[int(tmp)])
    else:
        print(d[tmp])