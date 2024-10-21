import sys

input = sys.stdin.readline

case = int(input())
dp = [0, 1, 1, 1, 2, 2]

for _ in range(case):
    n = int(input())
    for i in range(len(dp), n + 1):
        dp.append(dp[i - 1] + dp[i - 5])
    print(dp[n])