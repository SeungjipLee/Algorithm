import sys
input = sys.stdin.readline
'''
n이 10이하인데 완탐 해도 될듯
'''
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
res = 1e9
def back(곱, 합, depth, start):
    global res
    if depth > 0:
        res = min(res, abs(곱-합))
    for i in range(start, n):
        back(곱 * ls[i][0], 합 + ls[i][1], depth + 1, i + 1)

back(1, 0, 0, 0)
print(res)