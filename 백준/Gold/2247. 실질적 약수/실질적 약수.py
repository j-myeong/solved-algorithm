n = int(input())
sum = 0
for i in range(2, n // 2 + 1):
    sum += (n // i - 1) * i
print(sum % 1000000)