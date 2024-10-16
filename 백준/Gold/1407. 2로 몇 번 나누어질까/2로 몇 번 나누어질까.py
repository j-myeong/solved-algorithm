a, b = map(int, input().split())
a -= 1

tmp_a = a
for i in range(1, 99):
    tmp_a += (a // (2 ** i)) * (2 ** (i - 1))

tmp_b = b
for i in range(1, 99):
    tmp_b += (b // (2 ** i)) * (2 ** (i - 1))

answer = tmp_b - tmp_a
print(answer)