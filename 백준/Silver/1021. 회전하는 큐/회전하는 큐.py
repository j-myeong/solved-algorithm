from collections import deque
import sys

input = sys.stdin.readline

tmp = input().rstrip().split(' ')
n, case = int(tmp[0]), int(tmp[1])

que = deque([i + 1 for i in range(n)])

tmp = input().rstrip().split(' ')
targets = [int(item) for item in tmp]

result = 0

for target in targets:
  cond_2 = 0
  cond_3 = 0
  pos = que[0]
  if pos == target:
    que.popleft()
  else:
    while(True):
      que.rotate(1)
      cond_3 += 1
      if que[0] == target:
        que.rotate(-cond_3)
        break
    while(True):
      que.rotate(-1)
      cond_2 += 1
      if que[0] == target:
        que.rotate(cond_2)
        break
    
    que.rotate(cond_3) if cond_2 > cond_3 else que.rotate(-cond_2)
    que.popleft()
    
    result += min(cond_2, cond_3)

print(result)