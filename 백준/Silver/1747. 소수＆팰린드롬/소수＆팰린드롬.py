import math

def pelindrome(n):
    n = str(n)
    return n == n[::-1]

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0): return False
    return True

n = int(input())

while True:
    if n == 1: 
        print(2)
        break
    if (pelindrome(n) and prime(n)):
        print(n)
        break
    n += 1