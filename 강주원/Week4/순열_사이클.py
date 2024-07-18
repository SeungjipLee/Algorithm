from collections import deque
t = int(input())

def sol():
    n = int(input())
    ls = [0] + list(map(int, input().split()))
    visit = [0] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if visit[i]:
            continue
        visit[i] = 1
        k = ls[i]
        temp = []
        temp.append(k)
        cnt += 1
        while temp:
            now = temp.pop()
            visit[now] = 1
            next = ls[now]
            if not visit[next]:
                temp.append(next)
            else:
                break
        
    return cnt

for tc in range(t):
    print(sol())
