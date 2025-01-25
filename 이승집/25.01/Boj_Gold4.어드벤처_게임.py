from collections import deque

def can_escape(rooms, graph):
    n = len(rooms)
    visited = [[False] * 501 for _ in range(n)]  # 최대 골드는 500까지 관리
    queue = deque([(0, 0)])  # (현재 방 번호, 현재 골드 양)
    visited[0][0] = True

    while queue:
        current, gold = queue.popleft()
        room_type, value = rooms[current]

        # 현재 방에서의 골드 업데이트
        if room_type == 'L':  # 골드를 얻는 방
            gold = max(gold, value)
        elif room_type == 'T':  # 골드를 요구하는 방
            if gold < value:  # 골드가 부족하면 탐색 불가
                continue
            gold -= value

        # 목적지 도달 확인
        if current == n - 1:
            return "Yes"

        # 다음 방 탐색
        for next_room in graph[current]:
            if not visited[next_room][gold]:  # 방문 여부 확인
                visited[next_room][gold] = True
                queue.append((next_room, gold))

    return "No"

while True:
    try:
        n = int(input())
        if n == 0:
            break

        rooms = []
        graph = [[] for _ in range(n)]
        for i in range(n):
            data = input().split()
            room_type, value, *connections = data
            rooms.append((room_type, int(value)))
            for conn in connections:
                if conn != '0':  # 연결된 방이 0이 아니면 추가
                    graph[i].append(int(conn) - 1)
        print(rooms, graph)
        print(can_escape(rooms, graph))
    except:
        break
