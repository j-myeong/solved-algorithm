n = int(input())
answer = []
for _ in range(n):
    answer.append(list(map(int, input().split())))

answer.sort()
for line in answer:
    print(*line)