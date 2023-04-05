import sys
input = sys.stdin.readline

x = int(input())

n = 1
sum = 0

while True:
  sum = int((n * (n + 1)) / 2)
  if sum >= x:
    break;
  else:
    n += 1

if n % 2 == 0:
  print(f'{n - (sum - x)}/{sum - x + 1}')
else:
  print(f'{sum - x + 1}/{n - (sum - x)}')