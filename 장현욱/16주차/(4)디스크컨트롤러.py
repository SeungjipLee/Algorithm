# 시작 순서대로 힙에 넣기(시작시간, 필요시간)
# 타이머 - 시작시간 + 필요시간 해서 나온게 한개의 완료까지 걸린 값
# 처음 들어간 힙을 순서대로 시작
# 시작시간 - 타이머 했을때 나온수가 작은게 1차비교, 걸리는 시간이 적은게 2차비교로 가야함.
# 1. 시작시간이 타이머보다 작은 수들을 다 꺼내서 다른 리스트에 넣기
# 2. 두번째 숫자를 기준으로 heapq 하기

import heapq
def solution(jobs):
    number = len(jobs)
    heapq.heapify(jobs)  # jobs의 시작시간 기준으로 정렬
    reservation = []  # 예약목록
    heapq.heapify(reservation)  # 힙 선언
    timer = jobs[0][0]
    alltime = 0

    while jobs or reservation:  # 해야할게 있는동안 진행
        while jobs and jobs[0][0] <= timer:
            now = heapq.heappop(jobs)
            heapq.heappush(reservation, (now[1], now[0]))  # 넣을때 뒤집기 걸리는시간, 시작시간

        if reservation:  # 해당 타이머의 작업량을 뽑아낸 후
            job_duration, job_start = heapq.heappop(reservation)
            if timer < job_start:  # 시간 공백이 있을경우를 생각한 조건문
                alltime += job_duration
                timer += job_duration
            else:
                alltime += timer + job_duration - job_start  # 현재시간 + 걸린시간 - 시작시간
                timer += job_duration
        else:
            timer = jobs[0][0]  # 다음 시작까지의 공백을 생각

    answer = alltime // number
    return answer


# for job in jobs:
    # heapq.heappush(heap, (job[1], job))