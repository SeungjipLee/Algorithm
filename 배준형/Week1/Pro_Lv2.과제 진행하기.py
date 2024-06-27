def solution(plans):
    answer = []
    sorted_plans = []
    for plan in plans:
        subject, start_time, remain_time = plan
        start_time = int(start_time[0:2])*60 + int(start_time[3:])
        remain_time = int(remain_time)
        sorted_plans.append([plan[0], start_time, remain_time])
    sorted_plans.sort(key=lambda x: x[1])
    
    stack = []
    top = -1
    cur_time = 0
    
    for plan in sorted_plans:
        subject, start, remain = plan
        if cur_time == 0:
            cur_time = start
            stack.append([subject, remain])
            continue
        while stack:
            prev_sub, prev_remain = stack.pop()
            if cur_time + prev_remain <= start:
                answer.append(prev_sub)
                cur_time += prev_remain
            else:
                stack.append([prev_sub, prev_remain-(start-cur_time)])
                break
        cur_time = start
        stack.append([subject, remain])
    
    while stack:
        subject, remain = stack.pop()
        answer.append(subject)
        
    return answer