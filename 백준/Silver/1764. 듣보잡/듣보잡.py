n, m = map(int, input().split())
p = set()
answer = []
for _ in range(n):
    p.add(input())
for _ in range(m):
    name = input()
    if name in p:
        answer.append(name)

print(len(answer))
answer.sort()
for name in answer: print(name)