import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

answer = [-1, -1]

def solution():
    n = int(input_())
    fruits = [0] + list(minput())
    adj_ls = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = minput()
        adj_ls[a].append(b)
        adj_ls[b].append(a)

    visited = [[False] * (n+1) for _ in range(n+1)]
    # print(adj_ls)

    for i in range(1, n+1):
        # print("start", i)
        dfs(i, fruits, adj_ls, visited, fruits[i])

    # 열매 갯수, 시작 정점 반환
    return answer 

def dfs(idx, fruits, adj_ls, visited, score):
    # print(idx, score)
    global answer
    if answer[0] < score:
        answer[0] = score
        answer[1] = idx
    elif answer[0] == score:
        answer[1] = min(answer[1], idx)
    
    for nxt in adj_ls[idx]:
        if visited[idx][nxt]:
            continue
        visited[idx][nxt] = True
        visited[nxt][idx] = True
        dfs(nxt, fruits, adj_ls, visited, score + fruits[nxt])
        visited[idx][nxt] = False
        visited[nxt][idx] = False
    

print(*solution())