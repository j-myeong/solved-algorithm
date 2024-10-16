n = int(input())
prefix = [-1001] * (n + 1)
arr = list(map(int, input().split()))

for i in range(n):
    prefix[i + 1] = max(prefix[i] + arr[i], arr[i])

print(max(prefix))