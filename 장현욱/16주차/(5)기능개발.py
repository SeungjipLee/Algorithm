# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
# 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 
# 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 
# return 하도록 solution 함수를 완성하세요.

from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)  # qee선언
    speeds = deque(speeds)
    day = 1  # 날짜 확인
    answer = []  # 정답 도출
    while progresses:  # 해야할 작업물이 남아있는동안 진행
        complete = 0  # 오늘 완료한 작업들
        while progresses[0] + speeds[0] * day >= 100:  # 완료했는지 판별
            progresses.popleft()
            speeds.popleft()
            complete += 1  # 완료
            if not progresses:  # 만약 리스트가 빈 경우엔 종료
                break
        if complete > 0:  # 완료한 작업이 있으면 기록
            answer.append(complete)
        day += 1
    return answer