answer = 0

def solution(k, dungeons):
    global answer    
    
    visited = [False] * k
    dfs(k, dungeons, 0, visited)
    
    return answer

def dfs(k, dungeons, d, visited):
    global answer
    
    for idx, dungeon in enumerate(dungeons):
        if visited[idx]:
            continue
        if k >= dungeon[0]:
            visited[idx] = True
            dfs(k-dungeon[1], dungeons, d+1, visited)
            visited[idx] = False
    else:
        answer = max(answer, d)
    