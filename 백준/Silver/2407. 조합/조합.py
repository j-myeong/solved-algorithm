from fractions import Fraction
import sys


def factorial(n):
    f = 1
    if n == 0:
        return 1
    while n != 1:
        f *= n
        n -= 1
    return f

input = sys.stdin.readline

tmp = input().split(' ')
n, r = int(tmp[0]), int(tmp[1])

print(Fraction(factorial(n), (factorial(r)*factorial(n-r))))