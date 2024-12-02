# n = 송전탑의 갯수
# wires = 연결된 송전탑

def DFS(start, graph, visited):
  count = 1  # 시작지점 노드
  stack = [start]  # 방문해야할곳들
  visited[start] = 1
  while stack:
    now = stack.pop()
    for nextPoint in graph[now]:
      if visited[nextPoint] == 0:
        stack.append(nextPoint)
        visited[nextPoint] = 1
        count += 1

  return count

def solution(n,  wires):
  answer = n-2
  for i in range(len(wires)):
    allMap = wires.copy()
    allGraph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    discount = allMap.pop(i)
    for j in allMap:
      x,y = j  # 파이썬이라 각각의 배열이 하나씩 담김
      allGraph[x].append(y)
      allGraph[y].append(x)

    a = DFS(1, allGraph, visited)
    b = n - a
    answer = min(answer, abs(a-b))

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