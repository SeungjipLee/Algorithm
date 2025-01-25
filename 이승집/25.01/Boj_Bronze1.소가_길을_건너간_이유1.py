N = int(input())
cnt = [-1] * 11
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    if cnt[a] != b and cnt[a] != -1:
        ans += 1
    cnt[a] = b
print(ans)