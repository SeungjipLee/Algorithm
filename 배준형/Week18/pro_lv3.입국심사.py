def solution(n, times):
    # 처음엔 모든 심사대가 비워져있다
    # 각 심사대는 걸리는 시간이 있다
    # 모든 사람이 심사를 받는데 걸리는 시간
    # 시간으로 접근
    answer = binary_search(n, times, 0, int(1e14))
    
    return answer

def binary_search(n, times, s, e):
    mid = (s + e)//2
    cnt = 0
    if s == e:
        return s
    
    for time in times:
        cnt += (mid//time)
    
    if cnt >= n:
        return binary_search(n, times, s, mid)
    else:
        return binary_search(n, times, mid+1, e)