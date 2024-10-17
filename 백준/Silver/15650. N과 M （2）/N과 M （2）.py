def recur(num, before):
    if num == end:
        print(*arr)
        return

    for i in range(1, n + 1):
        if i <= before: continue
        arr.append(i)
        recur(num + 1, i)
        arr.pop()

n, end = map(int, input().split())

arr = []
recur(0, 0)