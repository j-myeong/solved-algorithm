case = int(input())

for _ in range(case):
    num = int(input())
    i = 0
    for i in range(2, 1000001):
        if num % i == 0:
            print("NO")
            break
    if i == 1000000:
        print("YES")