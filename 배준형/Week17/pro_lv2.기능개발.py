from collections import defaultdict 
def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0
    for idx, progress in enumerate(progresses):
        works = (100-progress) // speeds[idx]
        if (100-progress) % speeds[idx]:
            works += 1
        if idx == 0:
            day = works
            cnt += 1
            continue
        if day >= works:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = works
    answer.append(cnt)
    return answer