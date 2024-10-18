import sys

input = sys.stdin.readline

def interview(idx, value):
    global answer

    if idx >= n:
        if idx > n: return;
        answer = max(answer, value)
        return;
    # 인터뷰 하는 경우
    interview(idx + data[idx][0], value + data[idx][1])
    # 인터뷰 안하는 경우
    interview(idx + 1, value)

n = int(input())
data = [list(map(int, input().strip().split())) for _ in range(n)]

answer = 0
interview(0, 0)
print(answer)