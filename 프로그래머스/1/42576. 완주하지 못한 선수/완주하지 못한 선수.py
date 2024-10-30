def solution(participant, completion):
    count = {}
    for name in participant:
        if name not in count:
            count[name] = 0
        count[name] += 1
    for name in completion:
        count[name] -= 1
        if count[name] == 0:
            del count[name]
    return list(count.keys()).pop()