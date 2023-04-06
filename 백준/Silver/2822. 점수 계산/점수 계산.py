import sys
from queue import PriorityQueue

input = sys.stdin.readline
data = PriorityQueue()
person = PriorityQueue()

for idx in range(8):
  data.put((-int(input()), idx + 1))

sum = 0
for _ in range(5):
  tmp = data.get()
  sum += (-tmp[0])
  person.put(tmp[1])

print(sum)
for _ in range(5):
  print(person.get(), end=' ')
