def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

test = int(input())

for _ in range(test):
    sum = 0
    tmp = input().split(' ')
    cnt = int(tmp[0])
    for i in range(cnt + 1):
        tmp[i] = int(tmp[i])
    
    for i in range(1, cnt):
        for j in range(i + 1, cnt + 1):
            sum += gcd(tmp[i], tmp[j])
    print(sum)