from collections import deque

total, start, goal, up, down = map(int, input().split())
if start == goal:
    print(0)
    exit()
    
direction = []
if up:
    direction.append(up)
if down:
    direction.append(-down)

visit = [0] * (total+1)
def sol(start):
    q = deque()
    q.append([start, 0])
    visit[start] = 1
    while q:
        now, cnt = q.popleft()
        for i in direction:
            next = now + i
            if next > total or next <= 0 or visit[next]:
                continue
            
            if next == goal:
                return cnt+1
            
            q.append([next,cnt+1])
            visit[next] = 1

    return 0

res = sol(start)

if res:
    print(res)
else:
    print("use the stairs")