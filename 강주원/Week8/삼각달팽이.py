'''
정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.
'''

'''
입출력 예
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
'''
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
    print(answer)
    return answer

solution(4)
'''
[0][0]
[1][0]
[2][0]
..
[n-1][0]
[n-1][1]
[n-1][2]
...
[n-1][n-1]
왼쪽이 1씩 늘어나다 n-1 에서 멈춘다
오른쪽이 1씩 늘어나다 n-1 에서 멈춘다
오른쪽이 1씩 줄어들다 1에서 멈춘다(한바퀴)
[2][1]...[n-2][1]
[n-2][n-2]
[n-3][2]
'''