case = int(input())

for _ in range(case):
  flag = True
  stack = []
  string = input()
  cnt = 0
  for char in string:
    cnt += 1
    if char == '(':
      stack.append('(')
    else:
      if not stack:
        flag = False
        break
      else:
        stack.pop()
  print('YES') if not stack and flag else print('NO')