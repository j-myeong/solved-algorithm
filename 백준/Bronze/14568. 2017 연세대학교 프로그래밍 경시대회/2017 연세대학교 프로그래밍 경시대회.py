n = int(input())
answer = 0
for a in range(1, n):
    for b in range(1, n):
        for c in range(b + 2, n):
            if a + b + c == n:
                if a % 2 == 1:
                    continue
                else:
                    answer += 1

print(answer)