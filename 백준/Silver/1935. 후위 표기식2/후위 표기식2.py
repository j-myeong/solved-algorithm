from curses.ascii import isalnum, isalpha
import sys


input = sys.stdin.readline

n = int(input())
form = input().rstrip()

stack = []

hash = {}

for idx in range(len(form)):
    if (form[idx].isalpha() and form[idx] not in hash):
        x = int(input())
        hash[form[idx]] = x
        stack.append(x)
    elif form[idx] in hash:
        stack.append(hash[form[idx]])
    else:
        right = stack.pop()
        left = stack.pop()
        if form[idx] == '*':
            stack.append(left * right)
        elif form[idx] == '/':
            stack.append(left / right)
        elif form[idx] == '+':
            stack.append(left + right)
        elif form[idx] == '-':
            stack.append(left - right)

print('%.2f' %stack.pop())