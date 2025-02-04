def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    board = [list(input()) for _ in range(n)]

    visited = [[0] * n  for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    ans = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == '1' and visited[i][j] == 0:
                mid = 0
                stack = [(i, j)]
                while stack:
                    nx, ny = stack.pop()
                    if visited[nx][ny] == 1:
                        continue
                    mid += 1
                    visited[nx][ny] = 1
                    for k in range(4):
                        new_x = nx + dx[k]
                        new_y = ny + dy[k]
                        if 0 <= new_x < n and 0 <= new_y < n and visited[new_x][new_y] == 0 and board[new_x][new_y] == '1':
                            stack.append((new_x, new_y))
                ans.append(mid)
    ans.sort()
    print(len(ans))
    for i in ans:
        print(i)



if __name__ == "__main__":
    main()