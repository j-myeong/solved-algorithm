import sys
input = sys.stdin.readline

case = int(input())
words = []

for _ in range(case):
  words.append(input().rstrip())

for word in words:
  check = []
  check.append(word[0])
  for at in range(1, len(word)):
    if word[at] in check and word[at - 1] != word[at]:
      case -= 1
      break
    elif word[at] not in check:
      check.append(word[at])

print(case)