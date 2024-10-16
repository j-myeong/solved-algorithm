import math

n = int(input())
nums = list(map(int, input().split()))
answer = 0
need_list = []
nums.sort()

for idx in range(n - 1):
    if math.gcd(nums[idx], nums[idx + 1]) != 1:
        need_list.append((nums[idx], nums[idx + 1]))

for start, end in need_list:
    for i in range(start + 1, end):
        if math.gcd(start, i) == 1 and math.gcd(end, i) == 1:
            answer += 1
            break
        if i == end - 1:
            answer += 2
print(answer)