    # 각각 높이가 다른 너비가 1 인 직사각형 N개가 나란히 정렬되어 있다
# 히스토그램에서 가장 큰 직사각형은?

# 아이디어 1
# 꼭대기들 에서 좌우로 퍼트리면서 크기 재보기

# 아이디어 2 V
# 최소높이 너비 체크해가면서 넓이 비교 계속하기
# 시작지점, 현재까지의 최솟값, 현재까지 너비 를 저장하고 한 칸 지날 때마다 꺼내서 갱신
# 현재 직사각형이 이전 직사각형보다 높이가 같거나 작으면 해당지점은 큐에 넣지 않음
# 어차피 이전 직사각형에서 계속 재기 때문에
# 

## 시간초과
import sys
from collections import deque
def minput(): return map(int, sys.stdin.readline().split())

while True:
    arr = list(minput())
    
    if arr[0] == 0:
        break
    
    N, *histogram = arr
    answer = 0
    q1 = deque()
    q2 = deque()

    for i in range(N):
        # [시작지점 s : start, 최소값 m : min, 현재너비 a : area]
        now = histogram[i]
        answer = max(answer, now)
        
        if i % 2 == 0:
            while q1:
                s, m, a =  q1.popleft()
                m = min(now, m)
                tmp_a = (i - s + 1) * m
                
                if a < tmp_a:
                    q2.append([s, m, tmp_a])
                    answer = max(answer, tmp_a)
            if i == 0 or now > histogram[i-1]:
                q2.append([i, now, now])
        else:
            while q2:
                s, m, a =  q2.popleft()
                m = min(now, m)
                tmp_a = (i - s + 1) * m
                
                if a < tmp_a:
                    q1.append([s, m, tmp_a])
                    answer = max(answer, tmp_a)
            if now > histogram[i-1]:        
                q1.append([i, now, now])

    print(answer)
        
        