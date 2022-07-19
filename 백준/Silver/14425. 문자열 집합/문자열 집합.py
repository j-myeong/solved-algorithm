tmp = input().split(' ')

n = int(tmp[0])
m = int(tmp[1])

dic = {}
sum = 0

for _ in range(n):
    tmp = input()
    dic[tmp] = True

for _ in range(m):
    tmp = input()
    if tmp in dic and dic[tmp]:
        sum += 1

print(sum)