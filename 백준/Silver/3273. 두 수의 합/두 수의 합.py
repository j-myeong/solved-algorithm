n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

left, right = 0, n - 1
answer = 0
while left < right:
    value = arr[left] + arr[right]
    if value == x:
        answer += 1
        left += 1
        right -= 1
    elif value < x:
        left += 1
    elif value > x:
        right -= 1

print(answer)