def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = []

tmp = input().split(' ')
for item in tmp:
    a.append(int(item))

x = int(input())

coprime = []

for item in a:
    if gcd(x, item) == 1:
        coprime.append(item)

result = sum(coprime) / len(coprime)
cond = sum(coprime) % len(coprime) == 0

print(int(result) if cond else result)