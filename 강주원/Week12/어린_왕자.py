'''
점과 점 사이의 거리가 반지름과 같거나 반지름 이하이면 원 내부에 있다
출발점 A를 포함한 원을 Ai
출발점 B를 포함한 원을 Bi라 했을 때
원의 합집합이 정답이 된다.
'''

import sys
input = sys.stdin.readline

t = int(input())


def sol():
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    A_circles = set()
    B_circles = set()
    for i in range(n):
        cx, cy, r = map(int, input().split())
        A_dist = (x1-cx)**2 + (y1-cy)**2
        B_dist = (x2-cx)**2 + (y2-cy)**2
        if A_dist <= r**2:
            A_circles.add(i)
        
        if B_dist <= r**2:
            B_circles.add(i)
        
    res = len(A_circles | B_circles) - len(A_circles & B_circles)
    print(res)

for tc in range(t):
    sol()
