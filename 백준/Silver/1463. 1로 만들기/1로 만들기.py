import sys
input = sys.stdin.readline

x = int(input())
dp = [-1] * (x + 1)
dp[1] = 0

for idx in range(2, x + 1):
    dp[idx] = dp[idx - 1] + 1
    if idx % 2 == 0:
        dp[idx] = min(dp[idx // 2] + 1, dp[idx])
    if idx % 3 == 0:
        dp[idx] = min(dp[idx // 3] + 1, dp[idx])
        
print(dp[x])