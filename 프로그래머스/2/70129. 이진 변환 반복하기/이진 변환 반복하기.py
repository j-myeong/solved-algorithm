def solution(s):
    zero_count = 0
    step = 0
    while len(s) > 1 and step != 5:
        step += 1
        before = len(s)
        s = s.replace('0', '')
        after = len(s)
        zero_count += before - after
        s = format(len(s), 'b')
    answer = [step, zero_count]
    return answer