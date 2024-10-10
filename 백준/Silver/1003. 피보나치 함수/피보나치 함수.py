t = int(input())
zero_call = [1, 0]
one_call = [0, 1]
for _ in range(t):
    n = int(input())
    if n >= len(zero_call):
        for i in range(len(zero_call), n + 1):
            zero_call.append(zero_call[i - 1] + zero_call[i - 2])
            one_call.append(one_call[i - 1] + one_call[i - 2])

    print(f"{zero_call[n]} {one_call[n]}")