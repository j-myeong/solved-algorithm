n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
count = 0
coin.reverse()
for c in coin:
    if c > k: continue
    count += k // c
    k -= (k // c) * c

print(count)