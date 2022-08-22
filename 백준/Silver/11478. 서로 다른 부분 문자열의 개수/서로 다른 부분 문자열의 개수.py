import sys

input = sys.stdin.readline

result = set()
tmp = input().rstrip()

for i in range(0, len(tmp)):
    for j in range(i + 1, len(tmp) + 1):
        result.add(tmp[i:j])

print(len(result))