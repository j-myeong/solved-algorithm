def recursive(count):
    if count == m:
        print(*answer)
        return

    for i in range(0, n):
        answer.append(num_arr[i])
        recursive(count + 1)
        answer.pop()

n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
num_arr.sort()
answer = []

recursive(0)