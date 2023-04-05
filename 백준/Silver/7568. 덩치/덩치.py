import sys

input = sys.stdin.readline

case = int(input())
data = []

for idx in range(case):
  person = input().split(' ')
  data.append((int(person[0]), int(person[1])))

result = [1 for _ in range(case)]

for i in range(case):
  for j in range(case):
    if i == j: continue
    if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
      result[i] += 1

for item in result:
  print(item, end=' ')