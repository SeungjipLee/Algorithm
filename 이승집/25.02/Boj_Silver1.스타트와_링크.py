ans = 1e9


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    adj = [list(map(int, input().split())) for _ in range(n)]

    def dfs(arr, r):
        team_A = []

        def dfs(start):
            global ans
            if len(team_A) == r:
                team_B = []
                cnt_A = 0
                cnt_B = 0
                for i in range(1, n+1):
                    if i not in team_A:
                        team_B.append(i)

                for a in team_A:
                    for b in team_A:
                        if a != b:
                            cnt_A += adj[a-1][b-1]

                for c in team_B:
                    for d in team_B:
                        if c != d:
                            cnt_B += adj[c-1][d-1]

                mid = abs(cnt_A - cnt_B)
                ans = min(mid, ans)
                return

            for i in range(start, len(arr)):
                team_A.append(arr[i])
                dfs(i+1)
                team_A.pop()
        dfs(0)

    dfs(list(range(1, n+1)), n//2)
    print(ans)




if __name__ == "__main__":
    main()

"""input
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
"""