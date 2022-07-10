import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
tmp = input().split(' ')
a = []

for item in tmp:
    a.append(int(item))

prime = []

for item in a:
    if item == 2:
        prime.append(item)
    else:
        flag = True
        for num in range(2, int(math.sqrt(item)) + 1):
            if item % num == 0:
                flag = False
                break
        if flag and item not in prime: prime.append(item)

if len(prime) == 0:
    print(-1)
elif len(prime) == 1:
    print(prime.pop())
else:
    sum = 1
    gcd_all = 0
    for idx in range(0, len(prime) - 1):
        gcd_all = gcd(prime[idx], prime[idx + 1])
    for item in prime:
        sum *= item
    print(sum // gcd_all)