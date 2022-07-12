test = int(input())

for _ in range(test):
    stack = []
    tmp = input()
    flag = True
    for char in tmp:
        if char == '(': stack.append('(')
        else:
            if len(stack) == 0:
                flag = False
                break
            else:
                stack.pop()
    print('YES' if flag and len(stack) == 0 else 'NO')