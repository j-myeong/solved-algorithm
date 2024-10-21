def calc_sec(pos):
    min, sec = map(int, pos.split(":"))
    return min * 60 + sec

def to_string(sec):
    min = sec // 60
    sec %= 60
    min = min if min >= 10 else f"0{min}"
    sec = sec if sec >= 10 else f"0{sec}"
    return f"{min}:{sec}"

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    pos = calc_sec(pos)
    op_start = calc_sec(op_start)
    op_end = calc_sec(op_end)
    video_len = calc_sec(video_len)

    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if command == "prev":
            pos = pos - 10 if pos >= 10 else 0
        elif command == "next":
            pos = pos + 10 if pos + 10 <= video_len else video_len
    
    if op_start <= pos <= op_end:
        pos = op_end

    
    return to_string(pos)