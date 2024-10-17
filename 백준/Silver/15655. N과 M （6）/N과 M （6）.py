def recursive(count, before):
    if count == m:
        print(*answer)
        return

    for i in range(before, n):
        if num_arr[i] in answer: continue
        answer.append(num_arr[i])
        recursive(count + 1, i)
        answer.pop()

n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
num_arr.sort()
answer = []

recursive(0, 0)