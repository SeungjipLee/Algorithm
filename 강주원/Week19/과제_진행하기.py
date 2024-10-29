def time_to_minute(time):
    minute = int(time[:2]) * 60 + int(time[3:])
    return minute

def solution(plans):
    answer = []
    plans.sort(key=lambda x:x[1])
    task = []
    for i in range(len(plans)-1):
        sub, start, time = plans[i]
        next_start = plans[i+1][1]
        start, next_start, time = time_to_minute(start), time_to_minute(next_start), int(time)
        # 과제 완료
        if start + time  <= next_start:
            answer.append(sub)
            자투리_시간 = next_start - (start+time)
            while task and 자투리_시간 > 0:
                task_time = task[-1][2]
                if 자투리_시간 >= task_time:
                    answer.append(task.pop()[0])
                    자투리_시간 -= task_time
                else:
                    task[-1][2] -= task_time
                    자투리_시간 = 0

        # 과제 미완료
        else:
            task.append(plans[i])
            plans[i][2] = time - (next_start - start)
            


    return answer

solution(	[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])
