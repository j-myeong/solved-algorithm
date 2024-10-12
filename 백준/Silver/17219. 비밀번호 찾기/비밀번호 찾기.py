import sys

input = sys.stdin.readline

n, m = map(int, input().split())
hash = {}
for _ in range(n):
    site, pw = input().strip().split()
    hash[site] = pw
for _ in range(m):
    print(hash[input().strip()])