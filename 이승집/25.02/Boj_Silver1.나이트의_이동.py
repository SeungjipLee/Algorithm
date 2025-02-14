def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    tc = int(input())

    dx = [-2, -2, -1, 1, 2, 2, 1, -1]
    dy = [-1, 1, 2, 2, 1, -1, -2, -2]

    for _ in range(tc):
        n = int(input())
        start_x, start_y = map(int, input().split())
        goal_x, goal_y = map(int, input().split())
        Q = deque([(start_x, start_y, 0)])
        visited =[[0] * n for _ in range(n)]
        visited[start_x][start_y] = 1

        while Q:
            now_x, now_y, val = Q.popleft()
            if now_x == goal_x and now_y == goal_y:
                print(val)
                break

            for k in range(8):
                nxt_x = now_x + dx[k]
                nxt_y = now_y + dy[k]
                if (0 <= nxt_x < n) and (0 <= nxt_y < n) and (visited[nxt_x][nxt_y] == 0):
                    visited[nxt_x][nxt_y] = 1
                    Q.append((nxt_x, nxt_y, val + 1))



if __name__ == "__main__":
    main()

"""input
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
"""