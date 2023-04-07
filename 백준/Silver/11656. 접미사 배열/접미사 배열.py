import sys
from collections import deque

input = sys.stdin.readline

prefix = []
word = input().rstrip()
deq = deque(list(word))

prefix.append(word)

while len(deq) > 1:
  deq.popleft()
  prefix.append(''.join(deq))

prefix.sort()

for item in prefix:
  print(item)