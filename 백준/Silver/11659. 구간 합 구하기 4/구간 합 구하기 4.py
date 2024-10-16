import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + nums[i - 1]
for _ in range(m):
    start, end = map(int, input().strip().split())
    print(prefix[end] - prefix[start - 1])
