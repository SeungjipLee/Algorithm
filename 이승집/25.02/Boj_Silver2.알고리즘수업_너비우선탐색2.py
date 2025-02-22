import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m, r = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    for ad in adj:
        ad.sort(reverse=True)

    answer = [0] * (n + 1)
    visited = [0] * (n + 1)
    visited[r] = 1
    Q = deque([r])
    step = 1
    while Q:
        now = Q.popleft()
        answer[now] = step
        step += 1

        for nxt in adj[now]:
            if visited[nxt] == 0:
                Q.append(nxt)
                visited[nxt] = 1


    for i in answer[1:]:
        print(i)


if __name__ == "__main__":
    main()


"""input
5 5 1
1 4
1 2
2 3
2 4
3 4
"""