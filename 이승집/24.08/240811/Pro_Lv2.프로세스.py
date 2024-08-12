from collections import deque

priorities = [5, 4, 3, 2, 1]
location = 4
answer = 0

"""
프로세스 4개
[A, B, C, D] - 프로세스
[2, 1, 3, 2] - 우선순위
 --------------------

정답 : C - D - A - B  

 A를 꺼내서 C가 우선순위가 더 높아 -> 꺼낸 A를 다시 넣어
 [B, C, D, A]
 
 B를 꺼내서 C가 우선순위가 더 높아 -> B 다시 넣어
 [C, D, A, B]
 
 C를 꺼내서 보니 우선순위가 더 높아 -> C 실행
 [D, A, B]
 
 그 다음 D
 [A, B]
 
 
 이제 알파벳을 넘어가면 어떻게 할 것인가?
 
 => (idx, 우선순위)
"""

Q = deque([(i, priorities[i]) for i in range(len(priorities))])
while Q:
    pick = Q.popleft()
    if Q:
        mid = max(Q, key=lambda x: x[1])[1]
        if pick[1] < mid:
            Q.append(pick)
        else:
            answer += 1
            if pick[0] == location:
                break
    else:
        answer += 1

print(answer)