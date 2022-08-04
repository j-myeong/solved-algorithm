import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0): return False
    return True

tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])

while m <= n:
    if m == 1: 
        print(2)
        m += 1
    else:
        if (prime(m)):
            print(m)
    m+= 1
