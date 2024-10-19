import sys

input = sys.stdin.readline

def bag(idx = 0, weight = 0):
    if weight > k:
        return -9999999999
    if idx == n:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max(bag(idx + 1, weight + items[idx][0]) + items[idx][1], bag(idx + 1, weight))
    return dp[idx][weight]

n, k = map(int,input().strip().split())
items = [list(map(int, input().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(100001)] for _ in range(n)]

answer = bag()
print(answer)