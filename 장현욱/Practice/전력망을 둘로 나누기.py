# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 
# 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 
# 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

# 송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 
# 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 
# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 
# solution 함수를 완성해주세요.

# n은 2 이상 100 이하인 자연수입니다.
# wires는 길이가 n-1인 정수형 2차원 배열입니다.
# wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 
# 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
# 1 ≤ v1 < v2 ≤ n 입니다.
# 전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

# def DFS(start, allG, visited):
#     count = 1
#     stack = [start]
#     visited[start] = 1
    
#     while stack:
#         now = stack.pop()
#         for nextPoint in allG[now]:
#             if visited[nextPoint] == 0:
#                 visited[nextPoint] = 1
#                 stack.append(nextPoint)
#                 count += 1
#     return count

def solution(n, wires):
    answer = n - 2
    
    for i in range(len(wires)):
        # 전체 맵
        allM = wires.copy()
        # 전체 그래프 칸 생성 몇번째가 몇번째와 연결되어있나 표시 EX) allG[1] = [2, 3] 1번째는 2와3과 연결되어있음
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

def DFS(start, allGraph, visited):
    count = 1  # 시작지점 노드는 포함이므로 1로 시작
    stack = [start]  # 1부터 시작하기때문에 출발지점 1로 시작
    visited[start] = 1  # 시작지점은 방문기록 찍기
    while stack:  # stack이 있는동안 계속 실행
        now = stack.pop()  # 스택에서 하나 꺼내서 현재위치
        for nextPoint in allGraph[now]:  # 현재 지점에서 연결된 리스트들 반복문 돌리기
            if visited[nextPoint] == 0:  # 방문 기록이 없다면
                stack.append(nextPoint)  # 다음 출발지점중 하나로 저장
                visited[nextPoint] = 1  # 방문기록찍기
                count += 1  # 카운트 증가
    return count  # 나온 카운트 반환

def solution(n,  wires):
    answer = n-2

    for i in range(len(wires)):  # 모든 와이어를 시도해보기 위한 반복문
      allMap = wires.copy() # 와이어 그대로 복사해서 지도 저장
      allGraph = [[]for i in range(n+1)]  # n+1개만큼 그래프를 그릴 리스트 만들기
      visited = [0] * (n+1)  # 방문한 리스트를 넣을방문기록 리스트
      discount = allMap.pop(i)  # 하나 끊고 시작
      for j in allMap:  # 그린 지도를 순회시작
          x, y = j  # 각 연결되어있는 와이어를 x와y에 넣고
          allGraph[x].append(y)  # x와이어는 y랑 연결되어 있다
          allGraph[y].append(x)  # y와이어는 x랑 연결되어있다
      
      # 탐색시작
      a = DFS(1, allGraph, visited)  # 깊이우선 탐색시작, 시작지점과 그려진 그래프, 방문기록 넘기기
      b = n - a  # 전체노드 - 나눠진 노드
      answer = min(answer, abs(a-b))  # 결과값이 더 작은걸 선택
    return answer