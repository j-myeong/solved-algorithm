tmp = input().split(' ')

n, k = int(tmp[0]), int(tmp[1])

table = [True] * (n + 1)
result = []

cnt = 0

for i in range(2, n + 1):
    flag = False
    if table[i]:
        cnt += 1
        if cnt == k:
            print(i)
            break
        result.append(i)
        for j in range(i * 2, n + 1, i):
            if table[j]:
                table[j] = False
                cnt += 1
                if cnt == k:
                    flag = True
                    print(j)
    if flag:
        break
