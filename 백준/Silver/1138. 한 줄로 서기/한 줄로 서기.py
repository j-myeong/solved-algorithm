import sys

input = sys.stdin.readline

case = int(input())
MAX = case + 1
result = [MAX for _ in range(case)]
hints = []

hints = input().strip().split(' ')
for idx in range(case):
  hints[idx] = int(hints[idx])

for hint_idx in range(len(hints)):
  cnt = 0
  pos = 0
  for idx in range(case):
    if idx == 0 and hints[hint_idx] == 0:
      break
    if result[idx] == MAX:
      cnt += 1
    if cnt == hints[hint_idx]:
      pos = idx + 1
      break
  for idx in range(pos, case):
    if result[idx] == MAX:
      pos = idx
      break
  result[pos] = str(hint_idx + 1)
print(' '.join(result))
