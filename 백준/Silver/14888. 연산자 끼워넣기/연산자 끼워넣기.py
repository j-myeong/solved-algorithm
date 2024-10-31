from itertools import permutations

def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '//':
        return -(abs(a) // abs(b)) if a < 0 or b < 0 else a // b

n = int(input())
arr = list(map(int, input().split()))
s = list(map(int, input().split()))

ops = []
for op, count in zip(['+', '-', '*', '//'], s):
    ops.extend([op] * count)

op_permutations = set(permutations(ops, n - 1))

max_ans = -float('inf')
min_ans = float('inf')

for p in op_permutations:
    result = arr[0]
    for op, num in zip(p, arr[1:]):
        result = calculate(op, result, num)
    
    max_ans = max(max_ans, result)
    min_ans = min(min_ans, result)

print(max_ans)
print(min_ans)