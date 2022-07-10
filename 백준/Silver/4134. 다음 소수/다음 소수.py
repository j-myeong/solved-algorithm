import math


test = int(input())


for _ in range(test):
    n = int(input())
    while True:
        if n < 2:
            print(2)
            break
        flag = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i) == 0:
                n += 1
                flag = False
                break
        if flag:
            print(n)
            break
