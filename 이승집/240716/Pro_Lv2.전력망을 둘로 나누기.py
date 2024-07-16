n = 4
wires = [[1,2],[2,3],[3,4]]
answer = 101

for case in range(n-1):
    # 한 줄씩 잘라보자
    temp = wires[case]
    wires.remove(temp)
    print(case)
    print(wires)

    # 인접행렬 작성
    Board = [[] for _ in range(n + 1)]
    for wire in wires:
        Board[wire[0]].append(wire[1])
        Board[wire[1]].append(wire[0])
    print(Board)

    # 숫자를 전부 방문해야하니 visted여부 체크
    start = wires[0][0]
    visited = [start]

    # DFS 방문해보자
    stack = [start]
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)

        for next in Board[now]:
            if next not in visited:
                stack.append(next)
    print(visited)

    # answer의 값이 더 크다면 작은 값으로 대체
    mid = abs(len(visited) * 2 - n)
    print(mid)
    if mid < answer:
        answer = mid

    # 자른 선 다시 복구
    wires.insert(case, temp)

print(answer)