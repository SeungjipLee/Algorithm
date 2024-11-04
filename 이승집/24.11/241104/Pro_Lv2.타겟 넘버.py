from itertools import product


def solution(numbers, target):
    answer = 0
    n = len(numbers)

    A = [[-1, 1] for _ in range(n)]
    for i in product(*A):
        mid = 0
        for j in range(n):
            mid += i[j] * numbers[j]
        if mid == target:
            answer += 1

    return answer


"""
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
    
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
"""