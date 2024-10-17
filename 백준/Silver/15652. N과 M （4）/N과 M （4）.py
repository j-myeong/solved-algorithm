def recursive(count, before):
    if count == m:
        print(*answer)
        return

    for i in range(before, n + 1):
        answer.append(i)
        recursive(count + 1, i)
        answer.pop()

n, m = map(int, input().split())
answer = []

recursive(0, 1)