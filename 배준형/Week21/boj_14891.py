import sys
from collections import deque
input_ = sys.stdin.readline
def lsinput(): return [int(i) for i in input_().rstrip()]

def solution():
    answer = 0
    # topni = [12시, 1시, 2시, ...]
    # topni 요소 = N극은 0, S극은 1
    topni = [deque(lsinput()) for _ in range(4)]
    # print(topni)
    K = int(input_())
    for _ in range(K):
        # print(topni)
        num, d = map(int, input_().split())
        num -= 1
        # 회전할 떄 보는건 인덱스 2, 6
        left, right = topni[num][6], topni[num][2]
        rotate(topni, num, d)

        # 1번 톱니
        if num == 0:
            if topni[1][6] != right:
                # 다르다면 2번 톱니 굴리기
                right = topni[1][2]
                rd = d * -1
                rotate(topni, 1, rd)
                if topni[2][6] != right:
                    # 다르다면 3번 톱니 굴리기
                    right = topni[2][2]
                    rd *= -1
                    rotate(topni, 2, rd)
                    if topni[3][6] != right:
                        # 다르다면 4번 톱니 굴리기
                        rd *= -1
                        rotate(topni, 3, rd)

        # 2번 톱니
        elif num == 1:
            if topni[2][6] != right:
                right = topni[2][2]
                rd = d * -1
                rotate(topni, 2, rd)
                if topni[3][6] != right:
                    rd *= -1
                    rotate(topni, 3, rd)
            if topni[0][2] != left:
                d *= -1
                rotate(topni, 0, d)

        # 3번 톱니
        elif num == 2:
            if topni[3][6] != right:
                rd = d * -1
                rotate(topni, 3, rd)
            if topni[1][2] != left:
                left = topni[1][6]
                d *= -1
                rotate(topni, 1, d)
                if topni[0][2] != left:
                    d *= -1
                    rotate(topni, 0, d)

        # 4번 톱니
        elif num == 3:
            if topni[2][2] != left:
                left = topni[2][6]
                d *= -1
                rotate(topni, 2, d)
                if topni[1][2] != left:
                    left = topni[1][6]
                    d *= -1
                    rotate(topni, 1, d)
                    if topni[0][2] != left:
                        d *= -1
                        rotate(topni, 0, d)
    # print(topni)
    if topni[0][0]:
        answer += 1
    if topni[1][0]:
        answer += 2
    if topni[2][0]:
        answer += 4
    if topni[3][0]:
        answer += 8

    return answer

def rotate(topni, num, d):
    if d == 1:
        topni[num].appendleft(topni[num].pop())
    elif d == -1:
        topni[num].append(topni[num].popleft())


print(solution())

# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

