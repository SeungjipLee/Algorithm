import math


def solution(progresses, speeds):
    answer = []
    times = []
    for i in range(len(progresses)):
        times.append(math.ceil((100 - progresses[i]) / speeds[i]))
    print(times)
    time = 0
    while times:
        time = times.pop(0)
        cnt = 1
        while times and times[0] <= time:
            times.pop(0)
            cnt += 1
        answer.append(cnt)

    return answer