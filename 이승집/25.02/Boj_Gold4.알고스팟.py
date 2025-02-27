import sys
import heapq


def main():
    input = sys.stdin.readline
    m, n = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    INF = float('inf')
    visited = [[INF] * m for _ in range(n)]
    visited[0][0] = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    pq = []
    heapq.heappush(pq, (0, 0, 0))

    while pq:
        val, ni, nj = heapq.heappop(pq)
        if ni == n-1 and nj == m-1:
            print(val)
            break

        for k in range(4):
            mi = ni + dx[k]
            mj = nj + dy[k]
            if (0 <= mi < n) and (0 <= mj < m) and (visited[mi][mj] > val + board[mi][mj]):
                visited[mi][mj] = val + board[mi][mj]
                heapq.heappush(pq, (val + board[mi][mj], mi, mj))

if __name__ == "__main__":
    main()

"""input
6 6
001111
010000
001111
110001
011010
100010
"""