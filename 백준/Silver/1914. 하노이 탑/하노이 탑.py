def hanoi(n, f, t, o):
    if n == 0: 
        return;
    hanoi(n - 1, f, o, t)
    print(f, t)
    hanoi(n - 1, o, t, f)

count = 1
n = int(input())
for _ in range(n - 1):
    count *= 2
    count += 1
print(count)

if n <= 20: hanoi(n, 1, 3, 2)
