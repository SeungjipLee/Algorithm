def solution(n):
    arr = [[0]*(i+1) for i in range(n)]
    goal = n*(n+1)//2
    def cycle():
        cnt = 1
        # 사이클 계수
        cycle_c = 0
        r = 0
        # 아래 오른쪽 위 순서
        while 1:
            for dir in ['d','r','u']:
                for i in range(n-cycle_c):
                    if dir == 'd':
                        arr[i+r*2][r] = cnt
                        cnt += 1
                        if cnt == goal+1:
                            return
                    elif dir == 'r':
                        arr[n-r-1][i+1+r] = cnt
                        cnt += 1
                        if cnt == goal+1:
                            return
                    elif dir == 'u':
                        arr[n-i-r-2][-1-r] = cnt
                        cnt += 1
                        if cnt == goal+1:
                            return
                cycle_c += 1
            r += 1
    cycle()
                
    answer = []
    for i in range(n):
        answer.extend(arr[i])
    return answer