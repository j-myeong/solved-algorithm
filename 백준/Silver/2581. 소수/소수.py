m = int(input())
n = int(input())

table = [True] * (n + 1)
result = []

for i in range(2, n + 1):
    if table[i]:
        if m <= i:
            result.append(i)
        for j in range(i * 2, n + 1, i):
            table[j] = False

sum_rt = sum(result)

if sum_rt:
    print(sum_rt)
    print(result[0])
else:
    print(-1)