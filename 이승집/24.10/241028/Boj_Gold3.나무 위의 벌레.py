import sys
from collections import deque

N = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))
graph = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def DFS(n):
    distances = [-1] * (N + 1)
    que = deque([[n, n]])
    distances[n] = [fruits[n - 1], [n, n]]

    maxDis = 0
    nodeList = []
    while que:
        print(distances)
        print(que)
        print(nodeList)
        print("-----------")
        route = que.pop()
        now = route[0]

        for next in graph[now]:
            if distances[next] == -1:
                temp = route[:]
                temp[0] = next
                dis = distances[now][0] + fruits[next - 1]
                distances[next] = [dis, temp]
                print("temp", temp)
                que.append(temp)
                if maxDis < dis:
                    maxDis = dis
                    nodeList = [next]
                elif maxDis == dis:
                    nodeList.append(next)
    same = {}
    for node in nodeList:
        same[node] = [distances[node][0], min(distances[node][1])]
    print("same", same)
    return same


dis = DFS(1)
print("--------")
print("dis", dis)
print("--------")
maxDis = -1
ansNode = -1
for node in dis:
    finalDis = DFS(node)
    for ans in finalDis:
        if maxDis < finalDis[ans][0]:
            maxDis = finalDis[ans][0]
            ansNode = finalDis[ans][1]
        if maxDis == finalDis[ans][0]:
            ansNode = min(finalDis[ans][1], ansNode)
if N == 1:
    print(fruits[0], 1)
else:
    print(maxDis, ansNode)

"""
6
1 1 1 1 1 1
1 3
2 3
3 4
3 5
5 6
"""