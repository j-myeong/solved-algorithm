def GCD(a, b):
    if a % b == 0: return b
    return GCD(b, a % b)

gcd, lcm = map(int, input().split())

last = int((gcd * lcm) ** 0.5)
min_sum = 1e9
min_a = 0
min_b = 0

for i in range(last, 1, -1):
    a = lcm * gcd // i
    b = i
    a, b = max(a, b), min(a, b)
    if a * b / gcd == lcm and GCD(a, b) == gcd:
        sum = a + b
        if sum <= min_sum:
            min_sum = sum
            min_a = a
            min_b = b
print(min_b, min_a)