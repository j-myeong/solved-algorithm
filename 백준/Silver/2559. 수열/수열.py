a, b = map(int, input().split())

arr = list(map(int, input().split()))
init_sum = sum(arr[:b])
sums = [init_sum]

for idx in range(b, a):
    sums.append(sums[-1] + arr[idx] - arr[idx - b])

print(max(sums))