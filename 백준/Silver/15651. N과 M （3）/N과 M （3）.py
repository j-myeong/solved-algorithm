def recursive(count):
    if count == m:
        print(*answer)
        return

    for i in range(1, n + 1):
        answer.append(i)
        recursive(count + 1)
        answer.pop()

n, m = map(int, input().split())
answer = []

recursive(0)