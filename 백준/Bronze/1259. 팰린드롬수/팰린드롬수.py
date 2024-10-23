import sys

input = sys.stdin.readline

tmp = input().strip()
while tmp != "0":
    answer = "yes"
    n = len(tmp)
    if n != 1:
        if n % 2 == 0:
            before = list(tmp[:n // 2])
            for char in tmp[n // 2:]:
                if before.pop() != char:
                    answer = "no"
                    break
        else:
            before = list(tmp[:n // 2])
            for char in tmp[n // 2 + 1:]:
                if before.pop() != char:
                    answer = "no"
                    break
    print(answer)
    tmp = input().strip()