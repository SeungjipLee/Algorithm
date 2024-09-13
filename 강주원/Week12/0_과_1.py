from collections import deque

t = int(input())

def bfs(n):
    q = deque()
    q.append([1 % n, '1'])
    visit = set()
    visit.add(1 % n)
    while q:
        remain, num = q.popleft()
        if  remain == 0:
            return num
        
        for i in ['0', '1']:
            next_num = num + i
            n_remain = (remain * 10 + int(i)) % n
            
            if n_remain in visit:
                continue
            
            visit.add(n_remain)
            q.append([n_remain, next_num])
    
    return "BRAK"


def sol(n):
    print(bfs(n))

for tc in range(t):
    sol(int(input()))

