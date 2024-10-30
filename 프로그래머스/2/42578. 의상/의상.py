def solution(clothes):
    answer = 1
    hash = {}
    for item, kind in clothes:
        if kind not in hash:
            hash[kind] = 0
        hash[kind] += 1
        
    for key in hash:
        answer *= hash[key] + 1
    return answer - 1