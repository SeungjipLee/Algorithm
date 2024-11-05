import sys
sys.setrecursionlimit(10000)
answer = int(1e9)

def solution(x, y, n):   
    global answer
    dfs(x, y, n, 0)
    
    if answer == int(1e9):
        return -1
    return answer

def dfs(x, y, n, d):
    global answer
    if x > y:
        return
    if x == y:
        answer = min(answer, d)
        return
    if d > answer:
        return
    
    if not y % 3:
        dfs(x, y//3, n, d+1)
    if not y % 2:
        dfs(x, y//2, n, d+1)
    dfs(x, y-n, n, d+1)