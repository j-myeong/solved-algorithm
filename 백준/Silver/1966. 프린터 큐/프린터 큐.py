from collections import deque
import sys

input = sys.stdin.readline

case = int(input())

for _ in range(case):
  p_que = deque()

  tmp = input().split(' ')
  n, m = int(tmp[0]), int(tmp[1])
  
  prints = input().rstrip().split(' ')

  for idx, level in enumerate(prints):
    p_que.append((idx, int(level)))
  
  result = 1
  while(p_que):
    flag = True
    tmp = p_que.popleft()
    for idx, level in p_que:
      if tmp[1] < level:
        flag = False
        break
    if not flag:
      p_que.append(tmp)
    else:
      if tmp[0] == m:
        break
      else:
        result += 1
  print(result)
    