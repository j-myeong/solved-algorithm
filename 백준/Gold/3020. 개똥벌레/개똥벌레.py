import sys

input = sys.stdin.readline

n, h = map(int, input().strip().split())
prefix = [0] * (h + 1)
for i in range(n):
    tmp = int(input().strip())

    if i % 2 == 0:
        prefix[0] += 1
        prefix[tmp] += -1

    else:
        prefix[-1] += -1
        prefix[h - tmp] += 1

for i in range(h):
    prefix[i + 1] = prefix[i] + prefix[i + 1]
prefix.pop()
find_value = min(prefix)
count = 0
for item in prefix:
    if item == find_value:
        count += 1

print(find_value, count)