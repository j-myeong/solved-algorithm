def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

tmp = input().split(' ')

a, b = int(tmp[0]), int(tmp[1])

gcd_ab = gcd(a, b)
lcm_ab = int((a * b) / gcd_ab)

print(gcd_ab)
print(lcm_ab)
