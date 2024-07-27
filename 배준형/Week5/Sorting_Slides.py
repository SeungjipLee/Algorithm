# 투명 슬라이드
# 투명 직사각형 필름에 각 번호가 적혀있는데
# 겹쳐있어서 어느 직사각형이 몇 번인지 모름
# 4 장이 있다하면
# A B C D 라는 직사각형 투명 종이가 있고
# 1 2 3 4 중 1개씩이 투명 종이에 적혀있음
# 종이와 번호를 매칭해서 출력하기
# Heap 1
# (A, 3) (B, 1) (C, 2) (D, 4)

# 풀이
# 각 종이마다 겹쳐서 보이는 숫자들 다 넣기
# ex) 
# A 종이에 1 2 4 
# B 종이에 1 3
# C 종이에 1 2 3
# D 종이에 3
# 순서대로 보면 D는 하나 밖에 없으니 확정
# D -> 3 이후 제거하면서 하나 밖에 안남은거
# B -> 1, C -> 2, A -> 4 

import sys
from collections import defaultdict, deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

test_case = 0
while True:
    test_case += 1
    N = int(input_())
    if N == 0:
        break
    
    slides = defaultdict(list)
    matchs = defaultdict(list)
    for i in range(N):
        slides[chr(65+i)].extend(list(minput()))
    for i in range(N):
        x, y = minput()
        for slide in slides:    
            if slides[slide][0] < x < slides[slide][1] and\
                slides[slide][2] < y < slides[slide][3]:
                    matchs[slide].append(i+1)     
                    matchs[i+1].append(slide)     
    
    goal = {}
    visited = {u : False for u in matchs}
    
    q = deque()
    for i in slides:
        if len(matchs[i]) == 1:
            q.append(i)
            goal[i] = matchs[i][0]
            visited[i] = True
            visited[matchs[i][0]] = True
            
    while q:
        now = q.popleft()
        # print(now)
        for nxt in matchs[now]:
            # print(nxt)
            # nxt 페이지숫자
            for page in matchs[nxt]:
                cnt = 0
                cur = -1
                for s in matchs[page]:
                    if visited[s]:
                        continue
                    cur = s
                    cnt += 1
                if cnt == 1:
                    q.append(page)
                    visited[page] = True
                    visited[cur] = True
                    goal[page] = cur
    
    print("Heap", test_case)
    if len(goal) == N:
        for i in range(N):
            print("("+chr(i+65)+","+str(goal[chr(i+65)])+")", end=" ")
        print()
    else:
        print("none")
    print()