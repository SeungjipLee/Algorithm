'''

7 6 4 2 1
6 5 4 2 1
5 4 4 2 1
4 3 4 2 1
3 3 3 2 1
2 2 3 2 1
2 2 2 1 1
1 1 2 1 1
1 0 1 1 1
0 0 0 1 1
0 0 0 0 0
10분
1 0 4 2 1
6
4 2 1 1 0
2 0 1 1 0
8
1 0 0 1 0
9
내림차순 정렬
10 6 4 3 2 1
min(ls[0], ls[1])

'''
import heapq
n = int(input())
ls = list(map(int, input().split()))
hq = []
for i in ls:
    heapq.heappush(hq, -i)

res = 0
while hq:
    first = -heapq.heappop(hq)
    if hq:
        second = -heapq.heappop(hq)
        res += second
        heapq.heappush(hq, -(first-second))
    else:
        res += first
        break

if res <= 1440:
    print(res)
else:
    print(-1)