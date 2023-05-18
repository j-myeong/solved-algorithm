from queue import PriorityQueue

n = int(input())
case = sorted(list(map(int, input().split(' '))))
case = [sum(case[:i + 1]) for i in range(n)]

print(sum(case))