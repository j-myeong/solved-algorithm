def cook(idx, s, b, used):
    global answer
    if idx == n:
        if used != 0:
            answer = min(abs(s - b), answer)
        return

    # 재료를 넣는 경우
    cook(idx + 1, s * arr[idx][0], b + arr[idx][1], used + 1)

    # 안 넣는 경우
    cook(idx + 1, s, b, used)

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
answer = 10e10
cook(0, 1, 0, 0)
print(answer)

