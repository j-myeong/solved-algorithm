import sys

input = sys.stdin.readline

case = int(input())
words = [[] for _ in range(50)]

for _ in range(case):
  word = input().strip()
  if word in words[len(word) - 1]:
    continue
  words[len(word) - 1].append(word)

for group in words:
  if not len(group):
    continue
  group.sort()
  for word in group:
    print(word)
