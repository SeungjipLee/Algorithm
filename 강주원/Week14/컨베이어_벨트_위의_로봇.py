import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dur = deque(list(map(int, input().split())))

robots = deque([0] * n)

def sol():
    step = 0
    while 1:
        step += 1

        # 벨트 회전
        dur.rotate(1)
        robots.rotate(1)
        robots[-1] = 0

        # 로봇 이동
        for now in range(n-2, -1, -1):
            if robots[now] == 0:
                continue
            
            next = now+1

            if robots[next] == 1 or dur[next] == 0:
                continue

            dur[next] -= 1
            robots[now], robots[next] = 0, 1
        
        robots[-1] = 0


        # 로봇 올리기
        if dur[0] > 0:
            robots[0] = 1
            dur[0] -= 1

        if dur.count(0) >= k:
            break
    
    return step


print(sol())