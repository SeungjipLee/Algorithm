import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, K = minput()
cats = list(minput())
cats.sort()
visited = [False] * N
answer = 0

e = N-1
# for i in range(N):
#     if cats[i] + cats[e] > K:
#         break
s = 0

while True:
    if e == 0:
        break
    if visited[e]:
        e -= 1
        continue
    now = cats[e]
    visited[e] = True
    w = K - now

    # 최대한 오른쪽으로 커서 이동시키기
    while True:
        if cats[s] <= w and s < e:
            s += 1
            continue
        break
    # print("right completed")
    # 커서 왼쪽으로 이동시키기
    while True:
        if cats[s] <= w and not visited[s]:
            visited[s] = True
            answer += 1
            break
        else:
            if s == 0:
                break
            s -= 1
    # print("left completed")
    e -= 1

print(answer)