import sys

sys.setrecursionlimit(999999)

def interview(idx):
    if idx > n:
        return -99999999999
    if idx == n:
        return 0
    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = max(interview(idx + table[idx][0]) + table[idx][1], interview(idx + 1))
    return dp[idx]

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * (n + 1)
interview(0)
print(max(dp))