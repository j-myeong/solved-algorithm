n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((end, start))

meetings.sort()

answer = 1
last = meetings[0][0]

for end, start in meetings[1:]:
    if last <= start:
        last = end
        answer += 1

print(answer)