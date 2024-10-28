import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

answer = [-1, int(1e9)]

def solution():
    n = int(input_())
    fruits = [0] + list(minput())
    adj_ls = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = minput()
        adj_ls[a].append(b)
        adj_ls[b].append(a)

    visited = [False] * (n+1)

    visited[1] = True
    dfs(1, fruits, adj_ls, visited, fruits[1])
    visited[1] = False
    start = answer[1]
    print(answer)
    visited[start] = True
    dfs(start, fruits, adj_ls, visited, fruits[start])
    # 열매 갯수, 시작 정점 반환
    return answer 

def dfs(idx, fruits, adj_ls, visited, score):

    global answer
    if answer[0] < score:
        answer[0] = score
        answer[1] = idx
    elif answer[0] == score:
        answer[1] = min(answer[1], idx)
    
    for nxt in adj_ls[idx]:
        if visited[nxt]:
            continue
        visited[idx] = True
        dfs(nxt, fruits, adj_ls, visited, score + fruits[nxt])
        visited[idx] = False
    

print(*solution())