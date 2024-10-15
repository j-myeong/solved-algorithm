def solution(n):
    answer = 0
    start = 1
    while start <= n:
        count = 0
        for i in range(start, n + 1):
            count += i
            if count > n: break
            elif count == n:
                answer += 1
                break
        start += 1
    return answer