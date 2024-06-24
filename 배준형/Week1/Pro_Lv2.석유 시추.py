from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    oil_nums = [[0] * m for _ in range(n)]

    answer = 0
    oil_area = 1
    oil_count = {}
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0:
                continue
            if oil_nums[i][j] != 0:
                continue
                
            q = deque()
            oil_nums[i][j] = oil_area
            q.append([i, j])
            cnt = 1
            
            while q:
                x, y = q.popleft()
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx, ny = x+dx, y+dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if land[nx][ny] == 0:
                        continue
                    if oil_nums[nx][ny]:
                        continue
                    oil_nums[nx][ny] = oil_area
                    q.append([nx, ny])
                    cnt += 1 
            oil_count[oil_area] = cnt
            oil_area += 1
            
    for sichu in range(m):
        oils = []
        oil_amount = 0
        for i in range(n):
            pass
            if oil_nums[i][sichu] and oil_nums[i][sichu] not in oils:
                oils.append(oil_nums[i][sichu])
        
        for oil in oils:
            oil_amount += oil_count[oil]
        
        answer = max(oil_amount, answer)
                
    return answer