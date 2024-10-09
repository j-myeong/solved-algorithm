n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for i in range(n):
    arr[i] -= b
    answer += 1
    if arr[i] <= 0: continue
    if arr[i] % c == 0:
        answer += arr[i] // c
    else:
        answer += arr[i] // c + 1

print(answer)