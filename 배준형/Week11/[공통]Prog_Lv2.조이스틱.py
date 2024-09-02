dist = 0

def solution(name):
    global dist
    
    answer = 0
    name = list(name)
    n = len(name)
    visited = [False] * n
    
    for i in range(n):
        if name[i] == "A":
            visited[i] = True
        answer += alpha_cnt(name[i])

    visited[0] = True
    dist = n

    dfs(0, n, visited, 0)

    return answer + dist

def alpha_cnt(a):
    up = ord(a) - ord("A")
    down = ord("Z") - ord(a) + 1
    return min(up, down)

def dfs(idx, n, visited, d):
    global dist
    if d > n:
        return
    f, b = idx, idx
    # 오른쪽
    for i in range(1, n+1):
        f += 1
        if f >= n:
            f = 0
        if visited[f]:
            continue
        else:
            break
    else:
        dist = min(dist, d)
        # print(d)
    # 왼쪽
    for j in range(1, n+1):
        b -= 1
        if b < 0:
            b = n-1
        if visited[b]:
            continue
        else:
            break
    else:
        dist = min(dist, d)
        # print(d)

    visited[b] = True
    dfs(b, n, visited, d+j)
    visited[b] = False
    
    visited[f] = True
    dfs(f, n, visited, d+i)
    visited[f] = False

