def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for idx in range(min(len(A), len(B))):
        answer += A[idx] * B.pop()
    return answer