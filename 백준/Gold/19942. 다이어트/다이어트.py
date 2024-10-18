import sys

input = sys.stdin.readline

def cook(idx, p, f, s, v, price):
    global answer
    if idx == n:
        if mp <= p and mf <= f and ms <= s and mv <= v:
            if answer > price:
                ans_arr.clear()
                ans_arr.append(use.copy())
                answer = price
            elif answer == price:
                ans_arr.append(use.copy())
        return

    use.append(idx + 1)
    cook(idx + 1, p + arr[idx][0], f + arr[idx][1], s + arr[idx][2], v + arr[idx][3], price + arr[idx][4])
    use.pop()
    cook(idx + 1, p, f, s, v, price)

n = int(input())
mp, mf, ms, mv = map(int, input().strip().split())
arr = [tuple(map(int, input().strip().split())) for _ in range(n)]
use = []
answer = 10e9
ans_arr = []

cook(0, 0, 0, 0, 0, 0)

if ans_arr:
    ans_arr.sort()
    print(answer)
    print(*ans_arr[0])
else:
    print(-1)
