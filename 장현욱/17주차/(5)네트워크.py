def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]  # 방문지도 생성
    for com in range(n):
        if visited[com] == False:  # 만약 방문 기록이 없다면
            BFS(n, computers, com, visited)  # BFS로 값들을 보내기
            answer += 1  # 다돌면 하나의 내트워크이므로 +1
    return answer
    
def BFS(n, computers, com, visited):
    visited[com] = True  # 방문 기록체크
    queue = []  # 현재 노드가접촉하고 있는 노드들을 넣어둘 리스트
    queue.append(com)  # 지금 방문한 노드 추가
    
    while len(queue) != 0:  # 해당 접촉노드가 있는동안
        now_com = queue.pop(0)  # 지금 보고있는 컴퓨터
        visited[now_com] = True  # 방문한곳은 방문 표시하기
        for connect in range(n):
            if connect != now_com and computers[now_com][connect] == 1:  
                # 자신의 번호가 아니고, 해당 연결로가 이어져있을경우
                if visited[connect] == False:  # 방문기록이 없다면
                    queue.append(connect)
        