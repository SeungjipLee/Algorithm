N, M = map(int, input().split())

answer = []
visited = [0] * (N + 1)


def backtracking(arr):
    global N, M
    if len(answer) == M:
        print(*answer)
        return

    for i in range(1, N + 1):
        if arr[i] == 0:
            answer.append(i)
            arr[i] = 1
            backtracking(arr)
            arr[i] = 0
            answer.pop()


backtracking(visited)
