def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

test = int(input())
for _ in range(test):
    tmp = input().split(' ')
    a, b = int(tmp[0]), int(tmp[1])
    gcd_ab = gcd(a, b)
    print(int(a * b / gcd_ab))
