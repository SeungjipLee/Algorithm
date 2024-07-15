# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 
# 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 
# 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

# 송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 
# 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.


def DFS(start, allG, visited):
    # 어차피 딱 두개로 나뉘니까 1부터 시작해도 무방
    count = 1
    stack = [start]
    visited[start] = 1
    # 스택이 있는동안 유지
    while stack:
        now = stack.pop()
        for nextPoint in allG[now]:
            if visited[nextPoint] == 0:
                visited[nextPoint] = 1
                stack.append(nextPoint)
                count += 1
    return count

def solution(n, wires):
    answer = n - 2
    
    for i in range(len(wires)):
        # 전체 맵
        allM = wires.copy()
        # 전체 그래프 몇번째가 몇번째와 연결되어있나 표시 EX) allG[1] = [2, 3] 1번째는 2와3과 연결되어있음
        allG = [[]for i in range(n + 1)]
        # 방문 기록
        visited = [0] * (n+1)
        disconnect = allM.pop(i) # 첫번째 경우 끊기
        for j in allM:
            # i를 제외한 경우들 돌려가며 x,y대입
            x, y = j
            # allG[x,y]번째 그래프는 x 또는 y번째와 연결되어 있음을 표시.
            allG[x].append(y) # x는 y와 연결됨
            allG[y].append(x) # y는 x와 연결됨
        
        # 탐색
        a = DFS(1, allG, visited)
        b = n - a # 전체노트 - 반대의 노드
        answer = min(answer, abs(a - b))
            
        
    return answer