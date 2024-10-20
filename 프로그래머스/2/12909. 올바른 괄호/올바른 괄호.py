def solution(s):
    answer = True
    stack = []
    for char in s:
        if char == '(':
            stack.append(0)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
    if stack: answer = False
    return answer