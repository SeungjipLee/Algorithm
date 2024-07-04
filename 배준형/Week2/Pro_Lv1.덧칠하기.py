def solution(n, m, section):
    answer = 0
    i = 0
    for need_paint_area in section:
        if need_paint_area < i:
            continue
        i = need_paint_area
        answer += 1
        i += m
        
    return answer