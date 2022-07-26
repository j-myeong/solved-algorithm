n = int(input())
dp = ['SK', 'CY']
flag = 0
while n != 1:
    if n > 3:
        n -= 3
        flag = 0 if flag == 1 else 1
        continue
    if n > 1:
        n -= 1
        flag = 0 if flag == 1 else 1
        continue
print(dp[flag])
    
