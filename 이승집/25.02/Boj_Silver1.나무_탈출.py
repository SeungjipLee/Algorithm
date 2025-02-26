import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n = int(input())
    answer = 0
    adj = {i: [] for i in range(1, n + 1)}
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [0] * (n + 1)
    Q = deque([(1, 0)])
    visited[1] = 1
    while Q:
        now, step = Q.popleft()
        mid = 0
        for nxt in adj[now]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                Q.append((nxt, step + 1))
                mid += 1
        if mid == 0:
            answer += step

    if answer%2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

"""input
8
8 1
1 4
7 4
6 4
6 5
1 3
2 3
"""